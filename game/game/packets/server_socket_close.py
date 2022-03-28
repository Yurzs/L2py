from .base import GameServerPacket


class ServerSocketClose(GameServerPacket):
    type = cython.char(175)
    constant = cython.long(0)
    arg_order = ["type", "constant"]
