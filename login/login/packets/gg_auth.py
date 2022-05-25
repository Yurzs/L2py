from dataclasses import Field, dataclass, field

from common.ctype import ctype

from .base import LoginServerPacket


@dataclass(kw_only=True)
class GGAuth(LoginServerPacket):
    type: ctype.char = field(default=11, init=False, repr=False)
    reply: ctype.int = 1
    zero1: ctype.int = field(default=0, init=False, repr=False)
    zero2: ctype.int = field(default=0, init=False, repr=False)
    zero3: ctype.int = field(default=0, init=False, repr=False)
    zero4: ctype.int = field(default=0, init=False, repr=False)

    @classmethod
    def parse(cls, data, client):
        return cls(data[1:5])
