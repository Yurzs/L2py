from dataclasses import dataclass, field

from src.common.common.ctype import ctype
from src.game.game.models.character import Character
from src.game.game.models.structures.object.object import L2Object
from src.game.game.packets.base import GameServerPacket


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
