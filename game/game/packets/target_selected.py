import typing
from dataclasses import dataclass, field

from game.models.structures.object.object import L2Object
from game.models.structures.object.position import Position
from game.packets.base import GameServerPacket

if typing.TYPE_CHECKING:
    from game.session import GameSession


@dataclass
class TargetSelected(GameServerPacket):
    type: cython.char = field(default=41, init=False, repr=False)
    me: L2Object
    target: L2Object

    def encode(self, session: "GameSession"):
        encoded = self.type.encode()

        encoded.extend(
            [
                self.me.id,
                self.target.id,
                self.me.position.point3d.x,
                self.me.position.point3d.y,
                self.me.position.point3d.z,
            ]
        )
        return encoded
