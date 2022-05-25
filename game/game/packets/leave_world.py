from dataclasses import dataclass, field

from common.ctype import ctype
from game.packets.base import GameServerPacket


@dataclass(kw_only=True)
class LeaveWorld(GameServerPacket):
    type: ctype.int8 = field(default=126, init=False, repr=False)
