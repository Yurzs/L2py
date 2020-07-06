from .base import LoginClientPacket
from common.datatypes import Int8, Int32


class RequestServerList(LoginClientPacket):
    type = Int8(5)
    arg_order = ["type", "session_id1", "session_id2", "unknown"]

    def __init__(self, session_id1, session_id2):
        self.session_id1 = Int32(session_id1)
        self.session_id2 = Int32(session_id2)

    @classmethod
    def parse(cls, data, client):
        data = data[1:]
        session_id1_1 = data[0:4]
        session_id1_2 = data[4:8]
        return cls(session_id1_1, session_id1_2)
