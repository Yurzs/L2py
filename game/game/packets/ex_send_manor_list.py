from .base import GameServerPacket


class ExSendManorList(GameServerPacket):
    type = cython.char(254)
    arg_order = ["type", "constant", ""]  # TODO custom method
    constant = cython.int(27)
