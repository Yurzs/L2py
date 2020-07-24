from common.packet import add_length, Packet
from gameserver.crypt.xor import xor_encrypt_game


class GameServerPacket(Packet):

    @add_length
    @xor_encrypt_game
    # @add_padding()
    def encode(self, client):
        return self.body

    @classmethod
    def parse(cls, data, client):
        pass

    @classmethod
    def decode(cls, data, client, **kwargs):
        pass
