from .base import LoginServerPacket
from common.datatypes import Int8, Bytes, Int32


class LoginOk(LoginServerPacket):
    type = Int8(3)
    arg_order = ["type", "session_key1", "session_key2", "unknown"]

    def __init__(self, session_key1, session_key2):
        self.session_key1 = Int32(session_key1)
        self.session_key2 = Int32(session_key2)
        self.unknown = Bytes(
            b"\x00\x00\x00\x00" +
            b"\x00\x00\x00\x00" +
            b"\xEA\x03\x00\x00" +
            b"\x00\x00\x00\x00" +
            b"\x00\x00\x00\x00" +
            b"\x02\x00\x00\x00")
