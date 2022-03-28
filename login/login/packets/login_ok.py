from dataclasses import dataclass, field

import cython

from .base import LoginServerPacket


@dataclass
class LoginOk(LoginServerPacket):
    type: cython.char = field(default=3, repr=False, init=False)
    login_ok1: cython.int
    login_ok2: cython.int
    unknown_bytes: bytes = field(
        default=b"\x00\x00\x00\x00"
        b"\x00\x00\x00\x00"
        b"\xEA\x03\x00\x00"
        b"\x00\x00\x00\x00"
        b"\x00\x00\x00\x00"
        b"\x02\x00\x00\x00",
        init=False,
        repr=False,
    )
