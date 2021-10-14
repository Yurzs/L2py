from dataclasses import dataclass, field

from common.datatypes import Int8

from .base import GameServerPacket


@dataclass
class CharDeleteOk(GameServerPacket):
    type: Int8 = field(default=35, init=False, repr=False)
