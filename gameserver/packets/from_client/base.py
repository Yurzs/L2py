from common.packet import Packet
from common.utils.xor import xor_encrypt_game
from common.utils.xor import xor_decrypt_game


class GameClientPacket(Packet):
    mapper = {}
    skip_xor = False

    def encode(self, client):
        pass

    @classmethod
    @xor_decrypt_game
    def decode(cls, data, client, **kwargs):
        return super().decode(data, client)
