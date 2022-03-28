from dataclasses import dataclass, field

import cython

from .base import LoginServerPacket


@dataclass
class PlayOk(LoginServerPacket):
    type: cython.char = field(default=7, repr=False, init=False)
    play_ok1: cython.long
    play_ok2: cython.long
    unknown: cython.char = field(default=1, init=False, repr=False)
