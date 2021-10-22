from dataclasses import dataclass, field

from game.packets.base import GameServerPacket


@dataclass
class LeaveWorld(GameServerPacket):
    type: Int8 = field(default=126, init=False, repr=False)
