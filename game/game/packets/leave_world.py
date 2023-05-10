from typing import ClassVar

from common.ctype import ctype
from game.packets.base import GameServerPacket


class LeaveWorld(GameServerPacket):
    type: ctype.int8 = 126
