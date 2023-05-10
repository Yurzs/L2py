from common.ctype import ctype

from .base import LoginServerPacket


class PlayOk(LoginServerPacket):
    type: ctype.char = 7
    play_ok1: ctype.int32
    play_ok2: ctype.int32
    unknown: ctype.char = 1
