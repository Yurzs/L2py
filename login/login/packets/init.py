from dataclasses import dataclass, field

import cython

from login.packets.base import LoginServerPacket


@dataclass
class Init(LoginServerPacket):
    type: cython.char = field(default=0, init=False, repr=False)
    session_id: cython.int
    protocol_version: cython.int
    rsa_key: bytes
    unknown1: cython.uint = field(default=0x29DD954E, init=False, repr=False)
    unknown2: cython.uint = field(default=0x77C39CFC, init=False, repr=False)
    unknown3: cython.uint = field(default=0x97ADB620, init=False, repr=False)
    unknown4: cython.uint = field(default=0x07BDE0F7, init=False, repr=False)
    blowfish_key: bytes
    null_termination: cython.char = field(default=0, init=False, repr=False)
