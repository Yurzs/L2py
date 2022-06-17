from dataclasses import dataclass, field

from src.common.common.ctype import ctype

from .base import LoginServerPacket


@dataclass(kw_only=True)
class PlayFail(LoginServerPacket):
    type: ctype.char = field(default=6, init=False, repr=False)
    reason_id: ctype.char
