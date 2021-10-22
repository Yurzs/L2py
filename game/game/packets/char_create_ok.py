from dataclasses import dataclass, field

from .base import GameServerPacket


@dataclass
class CharCreateOk(GameServerPacket):
    type: Int8 = field(default=25, init=False, repr=False)
    result_ok: Int16 = field(default=1, init=False, repr=False)
