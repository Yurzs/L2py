from typing import ClassVar

from common.ctype import ctype
from common.misc import extend_bytearray
from login.packets.base import LoginServerPacket


class Init(LoginServerPacket):
    type: ctype.char = 0
    session_id: ctype.int32
    protocol_version: ctype.int32
    rsa_key: bytes
    unknown1: ctype.uint = 0x29DD954E
    unknown2: ctype.uint = 0x77C39CFC
    unknown3: ctype.uint = 0x97ADB620
    unknown4: ctype.uint = 0x07BDE0F7
    blowfish_key: bytes
    null_termination: ctype.char = 0
