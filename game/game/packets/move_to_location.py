from typing import ClassVar

from common.ctype import ctype

from .base import GameServerPacket


class MoveToLocation(GameServerPacket):
    type: ctype.int8 = 1

    object_id: ctype.int32
    destination_x: ctype.int32
    destination_y: ctype.int32
    destination_z: ctype.int32
    current_x: ctype.int32
    current_y: ctype.int32
    current_z: ctype.int32
