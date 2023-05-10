from typing import ClassVar

from common.ctype import ctype

from .base import GameServerPacket


class ActionFailed(GameServerPacket):
    type: ctype.int8 = 37
