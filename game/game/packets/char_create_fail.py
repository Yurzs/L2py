from dataclasses import dataclass, field

from common.datatypes import Int8, Int32

from .base import GameServerPacket


@dataclass
class CharCreateFail(GameServerPacket):
    type: Int8 = field(default=26, init=False, repr=False)
    reason_id: Int32
