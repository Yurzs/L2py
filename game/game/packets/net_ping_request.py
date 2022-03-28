from .base import GameServerPacket


class NetPingRequest(GameServerPacket):
    type = cython.char(211)
    arg_order = ["type", "ping_id"]

    def __init__(self, ping_id):
        self.ping_id = cython.long(ping_id)
