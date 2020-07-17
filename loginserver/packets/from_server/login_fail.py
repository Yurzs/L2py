from common.datatypes import Int32, Int8
from .base import LoginServerPacket


class Reason:
    SYSTEM_ERROR = Int8(1)
    WRONG_PASSWORD = Int8(2)
    WRONG_LOGIN_OR_PASSWORD = Int8(3)
    ACCESS_DENIED = Int8(4)
    DATABASE_ERROR = Int8(5)
    ACCOUNT_ALREADY_IN_USE = Int8(7)
    ACCOUNT_BANNED = Int8(9)
    MAINTENANCE = Int8(16)
    EXPIRED = Int8(18)
    TIME_IS_UP = Int8(19)


class LoginFail(LoginServerPacket):
    type = Int8(1)
    arg_order = ["type", "reason_id"]

    REASON = Reason

    def __init__(self, reason_id):
        self.reason_id = Int32(reason_id)
