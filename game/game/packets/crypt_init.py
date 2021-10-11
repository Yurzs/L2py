from dataclasses import dataclass, field

from common.datatypes import Bytes, Int8, Int32
from game.packets.base import GameServerPacket


@dataclass
class CryptInit(GameServerPacket):
    type: Int8 = field(default=0, repr=False, init=False)
    # unknown1: Int32 = field(default=1, repr=False, init=False)
    is_valid: Int8
    xor_key: Bytes
    unknown2: Int32 = field(default=16777216, repr=False, init=False)
    unknown3: Int32 = field(default=16777216, repr=False, init=False)
    # unknown4: Int8 = field(default=1, repr=False, init=False)
