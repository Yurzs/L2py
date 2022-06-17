import typing
from dataclasses import dataclass, field

from src.common.common.ctype import ctype
from src.game.game.static.character_template import StaticCharacterTemplate

from .base import GameServerPacket


@dataclass(kw_only=True)
class CharTemplates(GameServerPacket):
    type: ctype.int8 = field(default=23, init=False, repr=False)
    templates: typing.List[StaticCharacterTemplate] = ()

    def encode(self, session):
        result = bytearray(self.type)
        result.extend(ctype.int32(len(self.templates)))

        for template in self.templates:
            result.extend(template.encode())
        return result
