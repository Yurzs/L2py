from .base import GameServerPacket
from common.datatypes import Int8


class CharDeleteFail(GameServerPacket):
    type = Int8(36)
    arg_order = ["type"]
