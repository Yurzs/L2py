from .base import GameServerPacket


class LogoutOk(GameServerPacket):
    type = Int8(126)
    arg_order = ["type"]
