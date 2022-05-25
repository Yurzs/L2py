from common.ctype import ctype

from .base import GameServerPacket


class NetPingRequest(GameServerPacket):
    type: ctype.int8 = 211
    arg_order = ["type", "ping_id"]

    def __init__(self, ping_id):
        self.ping_id: ctype.int32 = ping_id
