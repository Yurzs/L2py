from common.datatypes import Int32, Int8
from .base import LoginServerPacket


class LoginFail(LoginServerPacket):
    type = Int8(1)
    arg_order = ["type", "reason_id"]

    def __init__(self, reason_id):
        self.reason_id = Int32(reason_id)
