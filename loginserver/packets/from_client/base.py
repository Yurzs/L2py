from common.packet import add_length, add_padding, Packet
from common.utils.checksum import add_checksum, verify_checksum
from common.utils.blowfish import blowfish_encrypt


class LoginClientPacket(Packet):

    @add_length
    @blowfish_encrypt()
    @add_checksum
    @add_padding()
    def encode(self, client):
        return self.body
