from common.datatypes import Int32, Int8
from .base import LoginServerPacket


class Reason:
    PASSWORD_MISMATCH = Int8(3)
    ACCESS_DENIED = Int8(4)
    TOO_MANY_USERS = Int8(15)


class PlayFail(LoginServerPacket):
    type = Int8(6)
    arg_order = ["type", "reason_id"]

    REASON = Reason

    def __init__(self, reason_id):
        self.reason_id = Int32(reason_id)
