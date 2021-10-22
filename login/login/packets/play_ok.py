from dataclasses import dataclass, field

from .base import LoginServerPacket


@dataclass
class PlayOk(LoginServerPacket):
    type: Int8 = field(default=7, repr=False, init=False)
    play_ok1: Int32
    play_ok2: Int32
    unknown: Int8 = field(default=1, init=False, repr=False)
