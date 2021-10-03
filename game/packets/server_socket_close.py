from common.datatypes import Int8, Int32

from .base import GameServerPacket


class ServerSocketClose(GameServerPacket):
    type = Int8(175)
    constant = Int32(0)
    arg_order = ["type", "constant"]
