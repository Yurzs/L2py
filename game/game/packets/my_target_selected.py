from typing import ClassVar

from common.ctype import ctype
from game.packets.base import GameServerPacket


class MyTargetSelected(GameServerPacket):
    type: ctype.int8 = 166
    object_id: ctype.int32
    color: ctype.int
