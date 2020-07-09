from common.datatypes import Int64, Int8
from common.helpers.bytearray import ByteArray
from .base import LoginClientPacket


class RequestServerLogin(LoginClientPacket):
    type = Int8(2)
    arg_order = ["type", "session_id1", "server_id"]

    def __init__(self, session_id1, server_id):
        self.session_id1 = Int64(session_id1)
        self.server_id = Int8(server_id)

    @classmethod
    def parse(cls, data, client):
        data = ByteArray(data[1:])
        session_id1 = data[0:8]
        server_id = data[8]
        return cls(session_id1, server_id)
