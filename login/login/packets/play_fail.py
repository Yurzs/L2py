from common.ctype import ctype

from .base import LoginServerPacket


class PlayFail(LoginServerPacket):
    type: ctype.char = 6
    reason_id: ctype.char
