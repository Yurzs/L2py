from common.datatypes import Bytes, Int32, Int8
from .base import GameServerPacket


class CryptInit(GameServerPacket):
    type = Int8(0)
    arg_order = ["type", "unknown1", "xor_key", "unknown2", "unknown3", "unknown4"]

    def __init__(self, xor_key, is_valid):
        self.unknown1 = Int8(1)
        self.id = Int8(is_valid)
        self.xor_key = Bytes(xor_key)
        self.unknown2 = Int32(1)
        self.unknown3 = Int32(1)
        self.unknown4 = Int8(1)

    @classmethod
    def parse(cls, data, client):
        pass

