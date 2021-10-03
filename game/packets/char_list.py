import typing
from dataclasses import dataclass, field
from common.datatypes import Int8, Int32
from common.helpers.bytearray import ByteArray
from data.models.character import Character
from .base import GameServerPacket


@dataclass
class CharList(GameServerPacket):
    type: Int8 = field(default=19, init=False, repr=False)
    characters: typing.List[Character] = ()

    def encode(self, client):
        arr = ByteArray(self.type.encode())
        arr.append(Int32(len(self.characters)))
        for character in self.characters:
            pass
        return arr
