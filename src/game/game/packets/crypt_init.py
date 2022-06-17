from dataclasses import dataclass, field

from src.common.common.ctype import ctype
from src.game.game.packets.base import GameServerPacket


@dataclass(kw_only=True)
class CryptInit(GameServerPacket):
    type: ctype.int8 = field(default=0, repr=False, init=False)
    # unknown1: ctype.int32 = field(default=1, repr=False, init=False)
    is_valid: ctype.int8
    xor_key: bytearray
    unknown2: ctype.int32 = field(default=16777216, repr=False, init=False)
    unknown3: ctype.int32 = field(default=16777216, repr=False, init=False)
    # unknown4: ctype.int8 = field(default=1, repr=False, init=False)
