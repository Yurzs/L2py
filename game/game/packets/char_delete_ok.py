from dataclasses import dataclass, field

from common.helpers.cython import cython

from .base import GameServerPacket


@dataclass
class CharDeleteOk(GameServerPacket):
    type: cython.char = field(default=35, init=False, repr=False)
