from common.datatypes import Int8
from .base import GameServerPacket


class CharDeleteOk(GameServerPacket):
    type = Int8(35)
    arg_order = ["type"]
