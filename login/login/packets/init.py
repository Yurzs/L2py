from dataclasses import dataclass, field

from common.datatypes import Bytes, Int8, Int32
from login.packets.base import LoginServerPacket


@dataclass
class Init(LoginServerPacket):
    type: Int8 = field(default=0, init=False, repr=False)
    session_id: Int32
    protocol_version: Int32
    rsa_key: Bytes
    unknown1: Int32 = field(default=0x29DD954E, init=False, repr=False)
    unknown2: Int32 = field(default=0x77C39CFC, init=False, repr=False)
    unknown3: Int32 = field(default=0x97ADB620, init=False, repr=False)
    unknown4: Int32 = field(default=0x07BDE0F7, init=False, repr=False)
    blowfish_key: Bytes
    null_termination: Int8 = field(default=0, init=False, repr=False)
