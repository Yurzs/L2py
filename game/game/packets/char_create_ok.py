from typing import ClassVar

from common.ctype import ctype

from .base import GameServerPacket


class CharCreateOk(GameServerPacket):
    type: ctype.int8 = 25
    result_ok: ctype.int8 = 1
