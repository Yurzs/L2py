from .base import GameServerPacket
from common.datatypes import Int8, Int32, Int16


class ExSendManorList(GameServerPacket):
    type = Int8(254)
    arg_order = ["type", "constant", ""]  # TODO custom method
    constant = Int16(27)

