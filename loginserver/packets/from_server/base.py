from common.packet import Packet, add_length, add_padding
from loginserver.crypt.blowfish import blowfish_encrypt, blowfish_decrypt
from loginserver.checksum import add_checksum


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

    @classmethod
    @blowfish_decrypt
    def decode(cls, data, client, **kwargs):
        packet_type = data[0]
        packet_cls = cls.mapper.get(packet_type)
        if packet_cls:
            return packet_cls.parse(data, client)
