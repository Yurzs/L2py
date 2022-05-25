from dataclasses import dataclass, field

from common.ctype import ctype
from login.packets.base import LoginServerPacket


@dataclass(kw_only=True)
class Init(LoginServerPacket):
    type: ctype.char = field(default=0, init=False, repr=False)
    session_id: ctype.int
    protocol_version: ctype.int
    rsa_key: bytes
    unknown1: ctype.uint = field(default=0x29DD954E, init=False, repr=False)
    unknown2: ctype.uint = field(default=0x77C39CFC, init=False, repr=False)
    unknown3: ctype.uint = field(default=0x97ADB620, init=False, repr=False)
    unknown4: ctype.uint = field(default=0x07BDE0F7, init=False, repr=False)
    blowfish_key: bytes
    null_termination: ctype.char = field(default=0, init=False, repr=False)
