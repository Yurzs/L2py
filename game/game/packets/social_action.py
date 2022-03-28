from dataclasses import dataclass, field

from game.models.structures.object.object import L2Object
from game.models.structures.object.position import Position
from game.packets.base import GameServerPacket


@dataclass
class SocialAction(GameServerPacket):
    type: cython.char = field(default=45, init=False, repr=False)

    character_id: cython.long
    action_id: cython.long
