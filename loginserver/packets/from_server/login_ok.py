from common.datatypes import Bytes, Int32, Int8
from .base import LoginServerPacket


class LoginOk(LoginServerPacket):
    type = Int8(3)
    arg_order = ["type", "login_ok1", "login_ok2", "unknown"]

    def __init__(self, login_ok1, login_ok2):
        self.login_ok1 = Int32(login_ok1)
        self.login_ok2 = Int32(login_ok2)
        self.unknown = Bytes(
            b"\x00\x00\x00\x00" +
            b"\x00\x00\x00\x00" +
            b"\xEA\x03\x00\x00" +
            b"\x00\x00\x00\x00" +
            b"\x00\x00\x00\x00" +
            b"\x02\x00\x00\x00")
