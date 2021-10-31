from dataclasses import dataclass, field

from game.models.structures.object.position import Position

from .base import GameServerPacket


@dataclass
class ChangeWaitType(GameServerPacket):
    type: Int8 = field(default=47, init=False, repr=False)

    character_id: Int32
    move_type: Int32
    position: Position

    def encode(self, session):
        encoded = self.type.encode()

        encoded.extend(
            [
                self.character_id,
                self.move_type,
                self.position.point3d.x,
                self.position.point3d.y,
                self.position.point3d.z,
            ]
        )
        return encoded
