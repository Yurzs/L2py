from common.datatypes import Int64, Int8, Int32, Bytes
from .base import LoginServerPacket


class PlayOk(LoginServerPacket):
    type = Int8(7)
    arg_order = ["type", "session_id2", "unknown"]

    def __init__(self, session_id2):
        self.session_id2 = Int64(session_id2)
        self.unknown = Bytes(b"\x01\x00\x00\x00\x00\x00\x00")

