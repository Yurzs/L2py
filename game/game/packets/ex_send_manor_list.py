from typing import ClassVar

from common.ctype import ctype

from .base import GameServerPacket


class ExSendManorList(GameServerPacket):
    type: ctype.int8 = 254
    constant: ctype.int8 = 27
