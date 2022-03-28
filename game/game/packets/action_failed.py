from dataclasses import dataclass, field

from common.helpers.cython import cython

from .base import GameServerPacket


@dataclass
class ActionFailed(GameServerPacket):
    type: cython.char = field(default=37, init=False, repr=False)
