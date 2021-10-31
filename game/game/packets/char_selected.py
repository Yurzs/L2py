import typing
from dataclasses import dataclass, field

import game.models.world
from game.models.character import Character
from game.packets.base import GameServerPacket

if typing.TYPE_CHECKING:
    from game.session import GameSession


@dataclass
class CharSelected(GameServerPacket):
    type: Int8 = field(default=21, init=False, repr=False)
    character: Character

    def encode(self, session: "GameSession"):
        """Encodes packet to bytearray."""

        encoded = self.type.encode()

        ordered_data = [
            self.character.name,
            self.character.id,
            self.character.title,
            session.id,
            Int32(0),  # TODO: clan id
            Int32(0),  # unknown
            self.character.sex,
            self.character.race,
            self.character.active_class,
            self.character.active,
            self.character.position.point3d.x,
            self.character.position.point3d.y,
            self.character.position.point3d.z,
            Double(self.character.status.hp.value),
            Double(self.character.status.mp.value),
            Double(self.character.status.cp.value),
            self.character.stats.exp,
            self.character.stats.level,
            self.character.stats.karma,
            self.character.stats.base.int,
            self.character.stats.base.str,
            self.character.stats.base.con,
            self.character.stats.base.men,
            self.character.stats.base.dex,
            self.character.stats.base.wit,
            *[Int32(0) for _ in range(32)],
            game.models.world.WORLD.clock.get_time(),
            *[Int32(0) for _ in range(18)],
        ]

        for item in ordered_data:
            encoded.append(item)
        return encoded
