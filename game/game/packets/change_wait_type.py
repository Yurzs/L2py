from dataclasses import dataclass, field

from common.helpers.cython import cython
from game.models.structures.object.position import Position

from .base import GameServerPacket


@dataclass
class ChangeWaitType(GameServerPacket):
    type: cython.char = field(default=47, init=False, repr=False)

    character_id: cython.long
    move_type: cython.long
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
