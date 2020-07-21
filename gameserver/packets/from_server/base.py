from common.packet import Packet, add_padding, add_length
from common.utils.xor import xor_encrypt_game
from common.utils.blowfish import blowfish_encrypt


class GameServerPacket(Packet):

    @add_length
    @xor_encrypt_game
    # @add_padding()
    def encode(self, client):
        return self.body
