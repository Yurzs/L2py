from common.datatypes import Int32, Int8
from .base import LoginServerPacket


class AccountKicked(LoginServerPacket):
    type = Int8(2)
    arg_order = ["type", "kick_reason"]

    def __init__(self, kick_reason_id):
        self.kick_reason = Int32(kick_reason_id)
