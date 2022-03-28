from dataclasses import dataclass, field

from game.models.structures.object.position import Position

from .base import GameServerPacket


@dataclass
class TeleportToLocation(GameServerPacket):
    type: cython.char = field(default=56, init=False, repr=False)

    character_id: cython.long
    position: Position

    def encode(self, session):
        encoded = self.type.encode()

        encoded.extend(
            [
                self.character_id,
                self.position.point3d.x,
                self.position.point3d.y,
                self.position.point3d.z,
            ]
        )
        return encoded
