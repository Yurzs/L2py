from .base import GameServerPacket


class LogoutOk(GameServerPacket):
    type = cython.char(126)
    arg_order = ["type"]
