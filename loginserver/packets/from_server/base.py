from common.packet import Packet, add_length, add_padding
from common.utils.blowfish import blowfish_encrypt
from common.utils.checksum import add_checksum


class LoginServerPacket(Packet):

    @add_length
    @blowfish_encrypt()
    @add_checksum
    @add_padding()
    def encode(self, client):
        return self.body

    @classmethod
    def parse(cls, data, client):
        pass
