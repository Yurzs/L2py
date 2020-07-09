from common.datatypes import Int64, Int8
from .base import LoginClientPacket


class RequestServerList(LoginClientPacket):
    type = Int8(5)
    arg_order = ["type", "session_id1"]

    def __init__(self, session_id1):
        self.session_id1 = Int64(session_id1)

    @classmethod
    def parse(cls, data, client):
        data = data[1:]
        session_id1 = data[0:8]
        return cls(session_id1)
