from dataclasses import dataclass, field

from common.ctype import ctype

from .base import LoginServerPacket


@dataclass(kw_only=True)
class LoginFail(LoginServerPacket):
    type: ctype.char = field(default=1, init=False, repr=False)
    reason_id: ctype.long
