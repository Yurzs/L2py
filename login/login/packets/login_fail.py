from dataclasses import dataclass, field

from .base import LoginServerPacket


@dataclass
class LoginFail(LoginServerPacket):
    type: Int8 = field(default=1, init=False, repr=False)
    reason_id: Int32
