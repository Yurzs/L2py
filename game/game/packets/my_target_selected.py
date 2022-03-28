from dataclasses import dataclass, field

from game.models.character import Character
from game.models.structures.object.object import L2Object
from game.packets.base import GameServerPacket


@dataclass
class MyTargetSelected(GameServerPacket):
    type: cython.char = field(default=166, init=False, repr=False)
    object_id: cython.long
    color: cython.int
