from common.packet import Packet


class GameServerPacket(Packet):
    def encode(self, client):
        return self.body

    @classmethod
    def parse(cls, data, client):
        pass

    @classmethod
    def decode(cls, data, client, **kwargs):
        pass
