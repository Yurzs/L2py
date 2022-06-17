import typing
from dataclasses import dataclass, field

from src.common.common.ctype import ctype
from src.common.common.misc import extend_bytearray
from src.game.game.models.structures.object.object import L2Object
from src.game.game.packets.base import GameServerPacket

if typing.TYPE_CHECKING:
    from src.game.game.session import GameSession


@dataclass(kw_only=True)
class TargetSelected(GameServerPacket):
    type: ctype.int8 = field(default=41, init=False, repr=False)
    me: L2Object
    target: L2Object

    def encode(self, session: "GameSession"):
        encoded = bytearray()

        extend_bytearray(
            encoded,
            [
                self.type,
                self.me.id,
                self.target.id,
                self.me.position.point3d.x,
                self.me.position.point3d.y,
                self.me.position.point3d.z,
            ],
        )
        return encoded
