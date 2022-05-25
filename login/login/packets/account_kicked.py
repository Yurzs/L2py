from common.ctype import ctype

from .base import LoginServerPacket


class Reason:
    DATA_STEALER: ctype.int8 = 1
    GENERIC_VIOLATION: ctype.int8 = 8
    SEVEN_DAYS_PASSED: ctype.int8 = 16
    ACCOUNT_BANNED: ctype.int8 = 32


class AccountKicked(LoginServerPacket):
    type: ctype.int8 = 2
    arg_order = ["type", "kick_reason"]

    REASON = Reason

    def __init__(self, kick_reason_id):
        self.kick_reason: ctype.int32 = kick_reason_id
