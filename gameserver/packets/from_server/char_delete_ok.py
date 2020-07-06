from .base import GameServerPacket
from common.datatypes import Int8


class CharDeleteOk(GameServerPacket):
    type = Int8(35)
    arg_order = ["type"]
