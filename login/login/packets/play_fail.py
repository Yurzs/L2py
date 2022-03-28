from dataclasses import dataclass, field

import cython

from .base import LoginServerPacket


@dataclass
class PlayFail(LoginServerPacket):
    type: cython.char = field(default=6, init=False, repr=False)
    reason_id: cython.char
