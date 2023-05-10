import logging
import time
from typing import TYPE_CHECKING, Union

from pydantic import Field

import game.constants
import game.packets
from common.application_modules.scheduler import ScheduleModule
from common.ctype import ctype
from common.model import BaseModel
from game.config import GameConfig
from game.models.structures.object.object import L2Object
from game.models.structures.object.position import Position
from game.models.structures.system_message import SystemMessage

if TYPE_CHECKING:
    from game.models.character import Character
    from game.session import GameSession

LOG = logging.getLogger(f"l2py.{__name__}")


class Clock(BaseModel):
    start_time: int = Field(default_factory=lambda: int(time.time()))
    TICKS_PER_SECOND = 10
    MSEC_IN_TICK = 1000 / TICKS_PER_SECOND

    _is_night = False

    @property
    def is_night(self):
        return self.hours < 6

    @property
    def hours(self):
        return (self.get_time() / 60) % 24

    @property
    def ticks(self):
        return ctype.int32(int(time.time()) - self.start_time / self.MSEC_IN_TICK)

    @staticmethod
    @ScheduleModule.job("interval", hours=3)
    async def daytime_change():
        CLOCK.toggle_is_night()

    def get_time(self):
        return ctype.int32(self.ticks / (self.TICKS_PER_SECOND * 10))

    def is_daytime_changed(self):
        return self._is_night != self.is_night

    def toggle_is_night(self):
        self._is_night = not self._is_night


CLOCK = Clock()


class World(BaseModel):
    _characters: dict["Character", "GameSession"] = {}
    _char_ids: dict[ctype.int32, "Character"] = {}
    _sessions: dict["GameSession", "Character"] = {}
    _objects: dict[ctype.int32, L2Object] = {}
    _parties = {}

    clock = CLOCK

    @property
    def characters(self):
        return list(self._characters)

    def get_character_by_id(self, char_id: ctype.int32) -> Union[None, "Character"]:
        return self._char_ids.get(char_id)

    def find_object_by_id(self, object_id: ctype.int32) -> Union[None, L2Object]:
        return self._objects.get(object_id)

    def get_session_by_character_name(self, char_name: str) -> Union[None, "GameSession"]:
        for char, session in self._characters.items():
            if char.name == char_name:
                return session

    @staticmethod
    def _inside_sphere(character, my_position, radius):
        return (
            (character.position.point3d.x.value - my_position.point3d.x.value)
            ^ 2 + (character.position.point3d.y.value - my_position.point3d.y.value)
            ^ 2 + (character.position.point3d.z.value - my_position.point3d.z.value)
            ^ 2
        ) < radius ^ 2

    def enter(self, session: "GameSession", character: "Character"):
        self._characters[character] = session
        self._char_ids[character.id] = character
        self._sessions[session] = character
        self._objects[character.id] = character

    def exit(self, session):
        character = self._sessions.pop(session)
        self._characters.pop(character)
        self._char_ids.pop(character.id)
        self._objects.pop(character.id)
        GameConfig().loop.create_task(
            character.commit_changes(
                fields=[
                    "position",
                    "status",
                    "stats",
                ]
            )
        )

    def notify_exit(self):
        pass  # TODO

    def players_sessions_nearby(
        self, position: Position, me: L2Object = None, radius=1000, specific_ids=()
    ):
        sessions = []
        for char, session in self._characters.items():
            if char.id in specific_ids:
                sessions.append(session)
                continue

            if me is None or char.id != me.id:
                if self._inside_sphere(char, position, radius):
                    sessions.append(session)
        return sessions

    def objects_nearby(self, me: L2Object):
        objects = []
        for char in self._characters:
            if char.id != me.id:
                if self._inside_sphere(char, me.position, 1000):
                    objects.append(char)
        return objects

    def notify_move(self, object_to_move, new_position):
        for session in self.players_sessions_nearby(object_to_move.position, object_to_move):
            session.send_packet(
                game.packets.CharMoveToLocation(
                    character=object_to_move, new_position=new_position
                )
            )

    def notify_spawn(self, character: "Character"):
        for session in self.players_sessions_nearby(character.position, character):
            session.send_packet(game.packets.CharInfo(character=character))
            session.send_packet(
                game.packets.CharMoveToLocation(
                    character=character, new_position=character.position
                )
            )

    def notify_me_about_others_nearby(self, session, character):
        for character in self.objects_nearby(character):
            session.send_packet(game.packets.CharInfo(character=character))
            session.send_packet(
                game.packets.CharMoveToLocation(
                    character=character, new_position=character.position
                )
            )

    def broadcast_snoop(
        self,
        creature: L2Object,
        text_type: ctype.int32,
        character_name: str,
        text: str,
    ):
        snoop = game.packets.Snoop(creature.id, creature.name, text_type, character_name, text)
        for session in self.players_sessions_nearby(creature.position, creature):
            session.send_packet(snoop)

    def broadcast_say(self, creature, packet):
        for session in self.players_sessions_nearby(creature.position, creature, radius=50):
            session.send_packet(packet)

    def say(self, creature, text_type, character_name, text, session=None):
        packet = game.packets.CreatureSay(
            object_id=creature.id,
            text_type=text_type,
            character_name=character_name,
            text=text,
        )
        if session is not None:
            session.send_packet(packet)
        self.broadcast_say(creature, packet)

    def startup(self):
        LOG.info("Creating the World.")

    def shutdown(self):
        LOG.info("World is shutting down")
        for session in self._characters.values():
            session.send_packet(game.packets.LeaveWorld())
            session.protocol.transport.close()

    def broadcast_sun_state(self):
        if self.clock.is_daytime_changed():
            pass  # TODO: night and day units spawn

    def _broadcast(self, me: L2Object, packet, also_for_me=True):
        for session in self.players_sessions_nearby(me.position, None if also_for_me else me, 700):
            session.send_packet(packet)

    def broadcast_target_select(self, me: L2Object, other: L2Object):
        for session in self.players_sessions_nearby(me.position, me, 500):
            session.send_packet(game.packets.TargetSelected(me, other))

    def broadcast_target_unselect(self, me):
        for session in self.players_sessions_nearby(me.position, me, 500):
            session.send_packet(
                game.packets.TargetUnselected(target_id=me.id, position=me.position)
            )

    def broadcast_attack(self, me: L2Object, attack_packet: "game.packets.Attack"):
        for session in self.players_sessions_nearby(me.position, me, 500):
            session.send_packet(attack_packet)

    def broadcast_action(self, me: L2Object, action_packet):
        for session in self.players_sessions_nearby(me.position, me, 500):
            session.send_packet(action_packet)

    @staticmethod
    def send_sys_message(character: "Character", message: SystemMessage):
        session = character.session
        if session is None:
            return

        session.send_packet(game.packets.SystemMessagePacket(message=message))


WORLD = World()
