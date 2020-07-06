from .base import GameServerPacket
from common.datatypes import Int8, Int32


class ServerSocketClose(GameServerPacket):
    type = Int8(175)
    constant = Int32(0)
    arg_order = ["type", "constant"]
    