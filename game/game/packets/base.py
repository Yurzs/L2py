from common.packet import Packet


class GameServerPacket(Packet):
    def encode(self, session, strings_format="utf-8"):
        return super().encode(session, strings_format=strings_format)

    @classmethod
    def parse(cls, data, client):
        pass

    @classmethod
    def decode(cls, data, client, **kwargs):
        pass
