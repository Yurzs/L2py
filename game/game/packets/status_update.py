from .base import GameServerPacket


class StatusUpdate(GameServerPacket):
    type = Int8(14)
    arg_order = ["type", "object_id", "stats_count"]
