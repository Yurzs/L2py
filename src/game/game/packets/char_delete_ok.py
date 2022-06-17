from dataclasses import dataclass, field

from src.common.common.ctype import ctype

from .base import GameServerPacket


@dataclass(kw_only=True)
class CharDeleteOk(GameServerPacket):
    type: ctype.int8 = field(default=35, init=False, repr=False)
