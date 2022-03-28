from dataclasses import dataclass, field

from game.packets.base import GameServerPacket


@dataclass
class CryptInit(GameServerPacket):
    type: cython.char = field(default=0, repr=False, init=False)
    # unknown1: cython.long = field(default=1, repr=False, init=False)
    is_valid: cython.char
    xor_key: Bytes
    unknown2: cython.long = field(default=16777216, repr=False, init=False)
    unknown3: cython.long = field(default=16777216, repr=False, init=False)
    # unknown4: cython.char = field(default=1, repr=False, init=False)
