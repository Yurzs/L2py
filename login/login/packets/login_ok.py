from common.ctype import ctype

from .base import LoginServerPacket


class LoginOk(LoginServerPacket):
    type: ctype.char = 3
    login_ok1: ctype.int32
    login_ok2: ctype.int32
    unknown_bytes: bytes = (
        b"\x00\x00\x00\x00"
        b"\x00\x00\x00\x00"
        b"\xEA\x03\x00\x00"
        b"\x00\x00\x00\x00"
        b"\x00\x00\x00\x00"
        b"\x02\x00\x00\x00"
    )
