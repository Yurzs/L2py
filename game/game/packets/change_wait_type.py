from dataclasses import dataclass, field

from common.ctype import ctype
from common.misc import extend_bytearray

from ..models.structures.object.position import Position
from .base import GameServerPacket


@dataclass(kw_only=True)
class ChangeWaitType(GameServerPacket):
    type: ctype.int8 = field(default=47, init=False, repr=False)

    character_id: ctype.int32
    move_type: ctype.int32
    position: Position

    def encode(self, session):
        encoded = bytearray()

        extend_bytearray(
            encoded,
            [
                self.type,
                self.character_id,
                self.move_type,
                self.position.point3d.x,
                self.position.point3d.y,
                self.position.point3d.z,
            ],
        )
        return encoded
