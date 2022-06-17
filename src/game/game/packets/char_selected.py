import typing
from dataclasses import dataclass, field

import src.game.game.models.world
from src.common.common.ctype import ctype
from src.common.common.misc import encode_str, extend_bytearray
from src.game.game.packets.base import GameServerPacket

if typing.TYPE_CHECKING:
    from src.game.game.models.character import Character
    from src.game.game.session import GameSession


@dataclass(kw_only=True)
class CharSelected(GameServerPacket):
    type: ctype.int8 = field(default=21, init=False, repr=False)
    character: "Character"

    def encode(self, session: "GameSession"):
        """Encodes packet to bytearray."""

        encoded = bytearray(self.type)

        extend_bytearray(
            encoded,
            [
                self.character.name,
                self.character.id,
                self.character.title,
                session.id,
                ctype.int32(0),  # TODO: clan id
                ctype.int32(0),  # unknown
                ctype.int32(self.character.appearance.sex),
                self.character.race,
                self.character.active_class,
                self.character.active,
                self.character.position.point3d.x,
                self.character.position.point3d.y,
                self.character.position.point3d.z,
                ctype.double(self.character.status.hp.value),
                ctype.double(self.character.status.mp.value),
                ctype.double(self.character.status.cp.value),
                self.character.stats.exp,
                self.character.stats.level,
                self.character.stats.karma,
                self.character.stats.base.INT,
                self.character.stats.base.STR,
                self.character.stats.base.CON,
                self.character.stats.base.MEN,
                self.character.stats.base.DEX,
                self.character.stats.base.WIT,
                *[ctype.int32(0) for _ in range(32)],
                game.models.world.WORLD.clock.get_time(),
                *[ctype.int32(0) for _ in range(18)],
            ],
        )

        return encoded
