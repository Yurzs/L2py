from .base import GameServerPacket
from common.datatypes import Int8


class CharCreateOk(GameServerPacket):
    type = Int8(19)
    arg_order = ["type", "static"]

    def __init__(self):
        self.static = Int8(1)
