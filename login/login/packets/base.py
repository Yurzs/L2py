import dataclasses

from common.packet import Packet


@dataclasses.dataclass(kw_only=True)
class LoginServerPacket(Packet):
    def encode(self, session):
        return self.body

    @classmethod
    def parse(cls, data, client):
        pass

    @classmethod
    def decode(cls, data, client, **kwargs):
        packet_type = data[0]
        packet_cls = cls.mapper.get(packet_type)
        if packet_cls:
            return packet_cls.parse(data, client)
