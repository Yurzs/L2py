from dataclasses import dataclass, field

from .base import GameServerPacket


@dataclass
class ActionFailed(GameServerPacket):
    type: Int8 = field(default=37, init=False, repr=False)
