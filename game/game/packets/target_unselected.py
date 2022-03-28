import typing
from dataclasses import dataclass, field

from game.models.structures.object.position import Position
from game.packets.base import GameServerPacket

if typing.TYPE_CHECKING:
    from game.session import GameSession


@dataclass
class TargetUnselected(GameServerPacket):
    type: cython.char = field(default=42, init=False, repr=False)
    target_id: cython.long
    position: Position

    def encode(self, session: "GameSession"):
        encoded = self.type.encode()

        ordered_data = [
            self.target_id,
            self.position.point3d.x,
            self.position.point3d.y,
            self.position.point3d.z,
        ]
        for item in ordered_data:
            encoded.append(item)
        return encoded
