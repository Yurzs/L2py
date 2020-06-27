from common.packet import Packet
from common.datatypes import Int
from collections import OrderedDict


class LoginFail(Packet):
    type = 1

    def __init__(self, reason_id):
        self.data = OrderedDict([
            ("reason_id", Int(reason_id)),
        ])

    @classmethod
    def parse(cls, packet_len, packet_type, data):
        pass
