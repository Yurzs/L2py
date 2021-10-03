from common.datatypes import Int8, Int32
from dataclasses import dataclass, field
from .base import GameServerPacket


@dataclass
class AuthLoginFail(GameServerPacket):
    type: Int8 = field(default=12, init=False, repr=False)
    reason_id: Int32
