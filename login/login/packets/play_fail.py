from dataclasses import dataclass, field

from common.datatypes import Int8

from .base import LoginServerPacket


@dataclass
class PlayFail(LoginServerPacket):
    type: Int8 = field(default=6, init=False, repr=False)
    reason_id: Int8
