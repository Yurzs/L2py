from typing import ClassVar

from common.ctype import ctype
from game.packets.base import GameServerPacket


class SocialAction(GameServerPacket):
    type: ctype.int8 = 45

    character_id: ctype.int32
    action_id: ctype.int32
