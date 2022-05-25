from dataclasses import dataclass, field

from common.ctype import ctype

from .base import GameServerPacket


@dataclass(kw_only=True)
class CharDeleteFail(GameServerPacket):
    type: ctype.int8 = field(default=36, init=False, repr=False)
