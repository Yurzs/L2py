from dataclasses import dataclass, field

from common.helpers.cython import cython

from .base import GameServerPacket


@dataclass
class AuthLoginFail(GameServerPacket):
    type: cython.char = field(default=12, init=False, repr=False)
    reason_id: cython.long
