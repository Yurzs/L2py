from common.datatypes import Bytes, Int32, Int8
from .base import GameServerPacket


class CryptInit(GameServerPacket):
    type = Int8(0)
    arg_order = ["unknown1", "xor_key", "unknown2", "unknown3"]

    def __init__(self, xor_key):
        self.unknown1 = Int8(1)
        self.xor_key = Bytes(xor_key)
        self.unknown2 = Int32(0)
        self.unknown3 = Int32(0)
