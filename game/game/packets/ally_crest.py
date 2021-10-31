from dataclasses import dataclass, field

from game.models.crest import Crest

from .base import GameServerPacket


@dataclass
class AllyCrest(GameServerPacket):
    type: Int8 = field(default=174, init=False, repr=False)
    crest: Crest

    def encode(self, session):
        encoded = self.type.encode()

        ordered_data = [
            self.crest.id,
            self.creast.size,
            self.crest.data,
        ]
        for item in ordered_data:
            encoded.append(item)
        return encoded
