import typing
from dataclasses import dataclass, field

from common.ctype import ctype
from common.misc import extend_bytearray
from game.models.structures.object.object import L2Object
from game.packets.base import GameServerPacket

if typing.TYPE_CHECKING:
    from game.session import GameSession


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
