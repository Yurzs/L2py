from common.datatypes import Int8, Int16

from .base import GameServerPacket


class ExSendManorList(GameServerPacket):
    type = Int8(254)
    arg_order = ["type", "constant", ""]  # TODO custom method
    constant = Int16(27)
