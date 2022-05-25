from dataclasses import dataclass, field

from common.ctype import ctype

from .base import GameServerPacket


@dataclass(kw_only=True)
class ActionFailed(GameServerPacket):
    type: ctype.int8 = field(default=37, init=False, repr=False)
