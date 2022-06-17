from src.common.common.ctype import ctype

from .base import GameServerPacket


class StatusUpdate(GameServerPacket):
    type: ctype.int8 = 14
    arg_order = ["type", "object_id", "stats_count"]
