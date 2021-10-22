from dataclasses import dataclass, field

from .base import GameServerPacket


@dataclass
class ChangeMoveType(GameServerPacket):
    type: Int8 = field(default=46, init=False, repr=False)

    character_id: Int32
    move_type: Int32
    constant: Int32 = field(default=0, init=False, repr=False)
