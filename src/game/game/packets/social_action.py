from dataclasses import dataclass, field

from src.common.common.ctype import ctype
from src.game.game.packets.base import GameServerPacket


@dataclass(kw_only=True)
class SocialAction(GameServerPacket):
    type: ctype.int8 = field(default=45, init=False, repr=False)

    character_id: ctype.int32
    action_id: ctype.int32
