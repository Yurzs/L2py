from typing import ClassVar

from common.ctype import ctype
from game.packets.base import GameServerPacket


class CryptInit(GameServerPacket):
    type: ctype.int8 = 0
    # unknown1: ctype.int32 = field(default=1, repr=False, init=False)
    is_valid: ctype.int8
    xor_key: bytearray
    unknown2: ctype.int32 = 16777216
    unknown3: ctype.int32 = 16777216
    # unknown4: ctype.int8 = field(default=1, repr=False, init=False)
