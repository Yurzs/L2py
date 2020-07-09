from common.datatypes import Int32, Int8
from common.packet import add_length, add_padding
from common.utils.blowfish import blowfish_encrypt
from .base import LoginServerPacket


class GGAuth(LoginServerPacket):
    type = Int8(11)
    arg_order = ["type", "reply"]

    def __init__(self):
        self.reply = Int32(11)

    async def answer(self, client):
        pass
