from common.datatypes import Int32, Int8
from common.packet import Packet


class LoginFail(Packet):
    type = Int8(1)
    arg_order = ["type", "reason_id"]

    def __init__(self, reason_id):
        self.reason_id = Int32(reason_id)
