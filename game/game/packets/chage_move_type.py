from dataclasses import dataclass, field

from common.ctype import ctype

from .base import GameServerPacket


@dataclass(kw_only=True)
class ChangeMoveType(GameServerPacket):
    type: ctype.int8 = field(default=46, init=False, repr=False)

    character_id: ctype.int32
    move_type: ctype.int32
    constant: ctype.int32 = field(default=0, init=False, repr=False)
