from common.datatypes import Int32, Int8
from .base import GameClientPacket


class ProtocolVersion(GameClientPacket):
    type = Int8(0)
    arg_order = ["type", "protocol_version"]

    def __init__(self, protocol_version):
        self.protocol_version = Int32(protocol_version)
