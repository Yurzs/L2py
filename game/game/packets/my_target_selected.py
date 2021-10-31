from dataclasses import dataclass, field

from game.models.character import Character
from game.models.structures.object.object import L2Object
from game.packets.base import GameServerPacket


@dataclass
class MyTargetSelected(GameServerPacket):
    type: Int8 = field(default=166, init=False, repr=False)
    object_id: Int32
    color: Int16
