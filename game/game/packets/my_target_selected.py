from dataclasses import dataclass, field

from common.ctype import ctype
from game.packets.base import GameServerPacket


@dataclass(kw_only=True)
class MyTargetSelected(GameServerPacket):
    type: ctype.int8 = field(default=166, init=False, repr=False)
    object_id: ctype.int32
    color: ctype.int
