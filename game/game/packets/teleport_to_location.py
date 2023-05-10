from typing import ClassVar

from common.ctype import ctype

from ..models.structures.object.position import Position
from .base import GameServerPacket


class TeleportToLocation(GameServerPacket):
    type: ctype.int8 = 56

    character_id: ctype.int32
    position: Position

    def encode(self, session):
        encoded = bytearray(self.type)

        encoded.extend(
            [
                self.character_id,
                self.position.point3d.x,
                self.position.point3d.y,
                self.position.point3d.z,
            ]
        )
        return encoded
