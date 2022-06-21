from dataclasses import dataclass, field

from common.ctype import ctype

from .base import LoginServerPacket


@dataclass(kw_only=True)
class PlayOk(LoginServerPacket):
    type: ctype.char = field(default=7, repr=False, init=False)
    play_ok1: ctype.int32
    play_ok2: ctype.int32
    unknown: ctype.char = field(default=1, init=False, repr=False)
