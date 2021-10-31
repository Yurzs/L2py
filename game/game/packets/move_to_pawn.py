from dataclasses import dataclass, field

from game.models.character import Character
from game.models.structures.object.object import L2Object
from game.packets.base import GameServerPacket

if typing.TYPE_CHECKING:
    from game.session import GameSession


@dataclass
class MoveToPawn(GameServerPacket):
    type: Int8 = field(default=96, init=False, repr=False)
    character: Character
    object: L2Object

    def encode(self, session):
        encoded = self.type.encode()

        ordered_data = [
            self.character.id,
            self.object.id,
        ]
