from .base import GameServerPacket
from common.datatypes import Int8


class LogoutOk(GameServerPacket):
    type = Int8(126)
    arg_order = ["type"]
