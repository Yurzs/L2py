import typing
from dataclasses import dataclass, field

from game.models.character import Character
from game.models.structures.object.position import Position
from game.packets.base import GameServerPacket

if typing.TYPE_CHECKING:
    from game.session import GameSession


@dataclass
class CharInfo(GameServerPacket):
    type: cython.char = field(default=3, init=False, repr=False)
    character: Character

    def encode(self, session: "GameSession"):
        encoded = self.type.encode()

        ordered_data = [
            self.character.position.point3d.x,
            self.character.position.point3d.y,
            self.character.position.point3d.z,
            self.character.position.heading_angle,
            self.character.id,
            self.character.name,
            self.character.race,
            self.character.sex,
            self.character.active_class,
            *self.character.inventory.encode_other(),
            *[cython.int(0) for _ in range(4)],
            # right hand augment
            self.character.inventory.equipped_items.right_hand.augmentation
            if self.character.inventory.equipped_items.right_hand is not None
            else cython.long(0),
            *[cython.int(0) for _ in range(12)],
            # left hand augment
            self.character.inventory.equipped_items.left_hand.augmentation
            if self.character.inventory.equipped_items.left_hand is not None
            else cython.long(0),
            *[cython.int(0) for _ in range(4)],
            cython.long(self.character.status.is_pvp),
            self.character.stats.karma,
            self.character.stats.magic_attack_speed,
            self.character.stats.physical_attack_speed,
            cython.long(self.character.status.is_pvp),
            self.character.stats.karma,
            self.character.stats.run_speed,
            self.character.stats.walk_speed,
            self.character.stats.run_speed,  # TODO SWIM SPEED
            self.character.stats.walk_speed,  # TODO SWIM SPEED
            self.character.stats.run_speed,  # TODO FL SPEED
            self.character.stats.walk_speed,  # TODO FL SPEED
            self.character.stats.run_speed,  # TODO FLY SPEED
            self.character.stats.walk_speed,  # TODO FLY SPEED
            self.character.stats.move_multiplier,
            self.character.stats.attack_speed_multiplier,
            self.character.template.collision_radius,
            self.character.template.collision_height,
            self.character.hair_style,
            self.character.hair_color,
            self.character.face,
            self.character.title if self.character.is_visible else UTFString("Invisible"),
            cython.long(0),  # TODO clan id
            cython.long(0),  # TODO clan crest id
            cython.long(0),  # TODO ally id
            cython.long(0),  # TODO ally crest id
            cython.long(0),
            cython.bint(not self.character.status.is_sitting),
            self.character.status.is_running,
            self.character.status.is_in_combat,
            self.character.status.is_faking_death,
            cython.bint(not self.character.is_visible),
            self.character.status.is_mounted,
            self.character.status.is_private_store,
            cython.int(0),  # TODO cubics
            cython.bint(0),  # 1 - to find party members
            cython.long(0),  # TODO abnormal effect
            self.character.stats.recommends_left,
            self.character.stats.recommends_received,
            self.character.base_class,
            self.character.stats.max_cp,
            self.character.status.cp,
            self.character.status.is_mounted,
            # TODO circles
            cython.char(0),  # TODO Team id
            cython.long(0),  # TODO clan large crest id
            self.character.status.is_noble,
            self.character.status.is_hero,
            self.character.status.is_fishing,
            cython.long(0),  # TODO fish x
            cython.long(0),  # TODO fish y
            cython.long(0),  # TODO fish z
            self.character.name_color,
            cython.long(self.character.status.is_running),
            cython.long(0),  # TODO pledge class
            cython.long(0),
            self.character.title_color,
            # TODO cursed weapons
            cython.long(0),
        ]
        for item in ordered_data:
            encoded.append(item)
        return encoded
