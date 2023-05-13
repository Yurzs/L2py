from common.packet import Packet


class LoginServerPacket(Packet):
    def encode(self, session, strings_format="utf-16-le"):
        return super().encode(session, strings_format="utf-16-le")

    @classmethod
    def parse(cls, data, client):
        pass

    @classmethod
    def decode(cls, data, client, **kwargs):
        packet_type = data[0]
        packet_cls = cls.mapper.get(packet_type)
        if packet_cls:
            return packet_cls.parse(data, client)
