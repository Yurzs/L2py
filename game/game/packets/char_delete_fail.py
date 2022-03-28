from dataclasses import dataclass, field

from common.helpers.cython import cython

from .base import GameServerPacket


@dataclass
class CharDeleteFail(GameServerPacket):
    type: cython.char = field(default=36, init=False, repr=False)
