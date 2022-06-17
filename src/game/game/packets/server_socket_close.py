from src.common.common.ctype import ctype

from .base import GameServerPacket


class ServerSocketClose(GameServerPacket):
    type: ctype.int8 = 175
    constant: ctype.int32 = 0
    arg_order = ["type", "constant"]
