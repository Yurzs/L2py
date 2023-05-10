from typing import ClassVar

from common.ctype import ctype

from .base import GameServerPacket


class ServerSocketClose(GameServerPacket):
    type: ctype.int8 = 175
    constant: ctype.int32 = 0
