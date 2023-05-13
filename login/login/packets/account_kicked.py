from typing import ClassVar

from common.ctype import ctype

from .base import LoginServerPacket


class Reason:
    DATA_STEALER: ctype.int8 = 1
    GENERIC_VIOLATION: ctype.int8 = 8
    SEVEN_DAYS_PASSED: ctype.int8 = 16
    ACCOUNT_BANNED: ctype.int8 = 32


class AccountKicked(LoginServerPacket):
    type: ctype.int8 = 2
    kick_reason: ctype.int32

    REASON: ClassVar[ctype.int8] = Reason
