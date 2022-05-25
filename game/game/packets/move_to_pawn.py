from dataclasses import dataclass, field

from common.ctype import ctype
from game.models.character import Character
from game.models.structures.object.object import L2Object
from game.packets.base import GameServerPacket


@dataclass(kw_only=True)
class MoveToPawn(GameServerPacket):
    type: ctype.int8 = field(default=96, init=False, repr=False)
    character: Character
    object: L2Object

    def encode(self, session):
        encoded = self.type.encode()

        ordered_data = [
            self.character.id,
            self.object.id,
        ]
