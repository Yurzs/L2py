from dataclasses import dataclass, field

import cython

from .base import LoginServerPacket


@dataclass
class LoginFail(LoginServerPacket):
    type: cython.char = field(default=1, init=False, repr=False)
    reason_id: cython.long
