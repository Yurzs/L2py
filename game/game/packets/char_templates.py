import typing
from dataclasses import dataclass, field

from common.helpers.bytearray import ByteArray
from game.models.character import Character
from game.static.character_template import StaticCharacterTemplate

from .base import GameServerPacket


@dataclass
class CharTemplates(GameServerPacket):
    type: cython.char = field(default=23, init=False, repr=False)
    templates: typing.List[StaticCharacterTemplate] = ()

    def encode(self, session):
        result = ByteArray(self.type)
        result.append(cython.long(len(self.templates)))

        for template in self.templates:
            result += template.encode()
        return result
