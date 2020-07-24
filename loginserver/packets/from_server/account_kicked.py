from common.datatypes import Int32, Int8
from .base import LoginServerPacket


class Reason:
    DATA_STEALER = Int8(1)
    GENERIC_VIOLATION = Int8(8)
    SEVEN_DAYS_PASSED = Int8(16)
    ACCOUNT_BANNED = Int8(32)


class AccountKicked(LoginServerPacket):
    type = Int8(2)
    arg_order = ["type", "kick_reason"]

    REASON = Reason

    def __init__(self, kick_reason_id):
        self.kick_reason = Int32(kick_reason_id)
