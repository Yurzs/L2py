from common.datatypes import Int8
from .base import GameServerPacket


class CharCreateOk(GameServerPacket):
    type = Int8(19)
    arg_order = ["type", "static"]

    def __init__(self):
        self.static = Int8(1)
