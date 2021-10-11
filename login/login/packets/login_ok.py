from dataclasses import dataclass, field

from common.datatypes import Bytes, Int8, Int32

from .base import LoginServerPacket


@dataclass
class LoginOk(LoginServerPacket):
    type: Int8 = field(default=3, repr=False, init=False)
    login_ok1: Int32
    login_ok2: Int32
    unknown_bytes: Bytes = field(
        default=b"\x00\x00\x00\x00"
        b"\x00\x00\x00\x00"
        b"\xEA\x03\x00\x00"
        b"\x00\x00\x00\x00"
        b"\x00\x00\x00\x00"
        b"\x02\x00\x00\x00",
        init=False,
        repr=False,
    )
