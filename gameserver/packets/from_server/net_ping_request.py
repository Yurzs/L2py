from .base import GameServerPacket
from common.datatypes import Int8, Int32


class NetPingRequest(GameServerPacket):
    type = Int8(211)
    arg_order = ["type", "ping_id"]

    def __init__(self, ping_id):
        self.ping_id = Int32(ping_id)
