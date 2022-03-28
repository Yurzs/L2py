from dataclasses import dataclass, field

from game.packets.base import GameServerPacket


@dataclass
class LeaveWorld(GameServerPacket):
    type: cython.char = field(default=126, init=False, repr=False)
