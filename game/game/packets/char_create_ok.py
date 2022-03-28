from dataclasses import dataclass, field

from common.helpers.cython import cython

from .base import GameServerPacket


@dataclass
class CharCreateOk(GameServerPacket):
    type: cython.char = field(default=25, init=False, repr=False)
    result_ok: cython.int = field(default=1, init=False, repr=False)
