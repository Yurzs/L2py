from typing import ClassVar

from common.ctype import ctype
from game.models.crest import Crest

from .base import GameServerPacket


class AllyCrest(GameServerPacket):
    type: ctype.int8 = 174
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
