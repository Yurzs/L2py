from common.packet import add_length, add_padding, Packet
from loginserver.checksum import add_checksum, verify_checksum
from loginserver.crypt.blowfish import blowfish_encrypt, blowfish_decrypt


class LoginClientPacket(Packet):

    @add_length
    @blowfish_encrypt()
    @add_checksum
    @add_padding()
    def encode(self, client):
        return self.body

    @classmethod
    @blowfish_decrypt
    @verify_checksum
    def decode(cls, data, client, **kwargs):
        packet_type = data[0]
        packet_cls = cls.mapper.get(packet_type)
        if packet_cls:
            return packet_cls.parse(data, client)
