from dataclasses import dataclass, field

import cython

from .base import LoginServerPacket


@dataclass
class GGAuth(LoginServerPacket):
    type: cython.char = field(default=11, init=False, repr=False)
    reply: cython.int = 1
    zero1: cython.int = field(default=0, init=False, repr=False)
    zero2: cython.int = field(default=0, init=False, repr=False)
    zero3: cython.int = field(default=0, init=False, repr=False)
    zero4: cython.int = field(default=0, init=False, repr=False)

    @classmethod
    def parse(cls, data, client):
        return cls(data[1:5])
