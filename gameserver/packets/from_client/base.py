from common.packet import Packet
from gameserver.crypt.xor import xor_decrypt_game


class GameClientPacket(Packet):
    mapper = {}
    skip_xor = False

    def encode(self, client):
        pass

    @classmethod
    @xor_decrypt_game
    def decode(cls, data, client, **kwargs):
        packet_type = data[0]
        packet_cls = cls.mapper.get(packet_type)
        if packet_cls:
            return packet_cls.parse(data, client)
