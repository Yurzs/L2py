from common.datatypes import Int32, Int8
from common.packet import add_length, add_padding
from common.utils.blowfish import blowfish_encrypt
from common.utils.checksum import verify_checksum
from .base import LoginServerPacket


class GGAuth(LoginServerPacket):
    type = Int8(11)
    arg_order = ["type", "reply", "zero1", "zero2", "zero3", "zero4"]

    def __init__(self, reply=1):
        self.reply = Int32(reply)
        self.zero1 = Int32(0)
        self.zero2 = Int32(0)
        self.zero3 = Int32(0)
        self.zero4 = Int32(0)

    async def answer(self, client):
        pass

    @classmethod
    @verify_checksum
    def parse(cls, data, client):
        return cls(data[1:5])
