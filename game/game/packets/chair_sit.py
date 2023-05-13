from typing import ClassVar

from common.ctype import ctype

from .base import GameServerPacket


class ChairSit(GameServerPacket):
    type: ctype.int8 = 225
    object_id: ctype.int32
    static_object_id: ctype.int32
