from dataclasses import dataclass, field

from common.helpers.cython import cython

from .base import GameServerPacket


@dataclass
class ChangeMoveType(GameServerPacket):
    type: cython.char = field(default=46, init=False, repr=False)

    character_id: cython.long
    move_type: cython.long
    constant: cython.long = field(default=0, init=False, repr=False)
