from typing import ClassVar

from common.ctype import ctype

from .base import GameServerPacket


class CharDeleteFail(GameServerPacket):
    type: ctype.int8 = 36
