from typing import ClassVar

from common.ctype import ctype

from .base import GameServerPacket


class AuthLoginFail(GameServerPacket):
    type: ctype.int8 = 12
    reason_id: ctype.int32
