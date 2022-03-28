from .base import GameServerPacket


class StatusUpdate(GameServerPacket):
    type = cython.char(14)
    arg_order = ["type", "object_id", "stats_count"]
