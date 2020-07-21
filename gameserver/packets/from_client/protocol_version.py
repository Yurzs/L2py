from common.datatypes import Int32, Int8
from .base import GameClientPacket


class ProtocolVersion(GameClientPacket):
    type = Int8(0)
    arg_order = ["type", "protocol_version"]
    skip_xor = True

    def __init__(self, protocol_version):
        self.protocol_version = Int32(protocol_version)

    @classmethod
    def parse(cls, data, client):
        version = Int32(data[1:5])
        return cls(version)
