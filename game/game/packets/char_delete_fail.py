from dataclasses import dataclass, field

from .base import GameServerPacket


@dataclass
class CharDeleteFail(GameServerPacket):
    type: Int8 = field(default=36, init=False, repr=False)
