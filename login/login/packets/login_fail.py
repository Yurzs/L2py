from common.ctype import ctype

from .base import LoginServerPacket


class LoginFail(LoginServerPacket):
    type: ctype.char = 1
    reason_id: ctype.long
