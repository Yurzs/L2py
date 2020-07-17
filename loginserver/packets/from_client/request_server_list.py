from common.datatypes import Int32, Int8
from .base import LoginClientPacket


class RequestServerList(LoginClientPacket):
    type = Int8(5)
    arg_order = ["type", "session_id1"]

    def __init__(self, login_ok1, login_ok2):
        self.login_ok1 = Int32(login_ok1)
        self.login_ok2 = Int32(login_ok2)

    @classmethod
    def parse(cls, data, client):
        data = data[1:]
        login_ok1 = data[0:4]
        login_ok2 = data[4:8]
        return cls(login_ok1, login_ok2)
