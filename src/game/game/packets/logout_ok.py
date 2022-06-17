from src.common.common.ctype import ctype

from .base import GameServerPacket


class LogoutOk(GameServerPacket):
    type: ctype.int8 = 126
    arg_order = ["type"]
