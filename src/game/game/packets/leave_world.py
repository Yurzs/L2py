from dataclasses import dataclass, field

from src.common.common.ctype import ctype
from src.game.game.packets.base import GameServerPacket


@dataclass(kw_only=True)
class LeaveWorld(GameServerPacket):
    type: ctype.int8 = field(default=126, init=False, repr=False)
