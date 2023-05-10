from typing import ClassVar

from common.ctype import ctype

from .base import GameServerPacket


class CharDeleteOk(GameServerPacket):
    type: ctype.int8 = 35
