from common.datatypes import Bytes, Int64, Int8
from .base import LoginServerPacket


class LoginOk(LoginServerPacket):
    type = Int8(3)
    arg_order = ["type", "session_key1", "unknown"]

    def __init__(self, session_key1):
        self.session_key1 = Int64(session_key1)
        self.unknown = Bytes(
            b"\x00\x00\x00\x00" +
            b"\x00\x00\x00\x00" +
            b"\xEA\x03\x00\x00" +
            b"\x00\x00\x00\x00" +
            b"\x00\x00\x00\x00" +
            b"\x02\x00\x00\x00")
