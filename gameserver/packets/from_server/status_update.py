from .base import GameServerPacket
from common.datatypes import Int8


class StatusUpdate(GameServerPacket):
    type = Int8(14)
    arg_order = ["type", "object_id", "stats_count"]

