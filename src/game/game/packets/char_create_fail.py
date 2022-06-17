from dataclasses import dataclass, field

from src.common.common.ctype import ctype

from .base import GameServerPacket


@dataclass(kw_only=True)
class CharCreateFail(GameServerPacket):
    type: ctype.int8 = field(default=26, init=False, repr=False)
    reason_id: ctype.int32
