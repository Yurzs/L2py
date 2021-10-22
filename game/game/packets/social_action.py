from dataclasses import dataclass, field

from data.models.structures.object.object import L2Object
from data.models.structures.object.position import Position
from game.packets.base import GameServerPacket


@dataclass
class SocialAction(GameServerPacket):
    type: Int8 = field(default=45, init=False, repr=False)

    character_id: Int32
    action_id: Int32
