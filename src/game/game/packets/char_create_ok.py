from dataclasses import dataclass, field

from src.common.common.ctype import ctype

from .base import GameServerPacket


@dataclass(kw_only=True)
class CharCreateOk(GameServerPacket):
    type: ctype.int8 = field(default=25, init=False, repr=False)
    result_ok: ctype.int = field(default=1, init=False, repr=False)
