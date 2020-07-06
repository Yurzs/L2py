from .base import LoginServerPacket, add_padding, add_length
from common.datatypes import Int8, Int32
from common.utils.blowfish import blowfish_encrypt


class GGAuth(LoginServerPacket):
    type = Int8(11)
    arg_order = ["type", "reply"]

    def __init__(self):
        self.reply = Int32(11)

    async def answer(self, client):
        pass

    @add_length
    @blowfish_encrypt()
    @add_padding()
    def encode(self, client):
        return self.body
