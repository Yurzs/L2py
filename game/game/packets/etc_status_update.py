import typing
from dataclasses import dataclass, field

from game.models.character import Character
from game.packets.base import GameServerPacket

if typing.TYPE_CHECKING:
    from game.session import GameSession


@dataclass
class EtcStatusUpdate(GameServerPacket):
    type: Int8 = field(default=243, init=False, repr=False)
    character: Character

    def encode(self, session: "GameSession"):
        encoded = self.type.encode()

        ordered_data = [
            self.character.weight_penalty,
            Int32(0),
            Int32(0),
            self.character.exp_penalty,
            self.character.exp_protected,
            self.character.death_penalty,
        ]

        for item in ordered_data:
            encoded.append(item)
        return encoded
