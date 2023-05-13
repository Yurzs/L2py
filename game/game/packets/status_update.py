from typing import ClassVar

from common.ctype import ctype

from .base import GameServerPacket


class StatusUpdate(GameServerPacket):
    type: ctype.int8 = 14
    object_id: ctype.int32
    stats_count: ctype.int32
