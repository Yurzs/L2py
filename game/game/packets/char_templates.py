from typing import ClassVar

from pydantic import Field

from common.ctype import ctype
from game.static.character_template import StaticCharacterTemplate

from .base import GameServerPacket


class CharTemplates(GameServerPacket):
    type: ctype.int8 = 23
    templates: list[StaticCharacterTemplate] = Field(default_factory=list)

    def encode(self, session):
        result = bytearray(self.type)
        result.extend(ctype.int32(len(self.templates)))

        for template in self.templates:
            result.extend(template.encode())
        return result
