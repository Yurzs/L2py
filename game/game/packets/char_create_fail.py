from typing import ClassVar

from common.ctype import ctype

from .base import GameServerPacket


class CharCreateFail(GameServerPacket):
    type: ctype.int8 = 26
    reason_id: ctype.int32
