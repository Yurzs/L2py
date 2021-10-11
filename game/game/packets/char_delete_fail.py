from common.datatypes import Int8

from .base import GameServerPacket


class CharDeleteFail(GameServerPacket):
    type = Int8(36)
    arg_order = ["type"]
