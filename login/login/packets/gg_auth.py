from dataclasses import dataclass, field

from .base import LoginServerPacket


@dataclass
class GGAuth(LoginServerPacket):
    type: Int8 = field(default=11, init=False, repr=False)
    reply: Int32 = 1
    zero1: Int32 = field(default=0, init=False, repr=False)
    zero2: Int32 = field(default=0, init=False, repr=False)
    zero3: Int32 = field(default=0, init=False, repr=False)
    zero4: Int32 = field(default=0, init=False, repr=False)

    @classmethod
    def parse(cls, data, client):
        return cls(data[1:5])
