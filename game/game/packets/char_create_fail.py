from dataclasses import dataclass, field

from common.helpers.cython import cython

from .base import GameServerPacket


@dataclass
class CharCreateFail(GameServerPacket):
    type: cython.char = field(default=26, init=False, repr=False)
    reason_id: cython.long
