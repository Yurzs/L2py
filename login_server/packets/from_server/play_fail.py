from .base import LoginServerPacket
from common.datatypes import Int8, Int32


class PlayFail(LoginServerPacket):
    type = Int8(6)
    arg_order = ["type", "reason_id"]

    def __init__(self, reason_id):
        self.reason_id = Int32(reason_id)
