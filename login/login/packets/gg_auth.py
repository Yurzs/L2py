from common.ctype import ctype

from .base import LoginServerPacket


class GGAuth(LoginServerPacket):
    type: ctype.char = 11
    reply: ctype.int32 = 1
    zero1: ctype.int32 = 0
    zero2: ctype.int32 = 0
    zero3: ctype.int32 = 0
    zero4: ctype.int32 = 0

    @classmethod
    def parse(cls, data, client):
        return cls(data[1:5])
