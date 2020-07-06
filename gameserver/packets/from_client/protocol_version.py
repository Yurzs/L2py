from .base import GameClientPacket
from common.datatypes import Int8, Int32


class ProtocolVersion(GameClientPacket):
    type = Int8(0)
    arg_order = ["type", "protocol_version"]

    def __init__(self, protocol_version):
        self.protocol_version = Int32(protocol_version)
