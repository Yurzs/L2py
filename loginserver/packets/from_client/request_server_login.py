from common.datatypes import Int32, Int8
from common.helpers.bytearray import ByteArray
from .base import LoginClientPacket
from common.utils.checksum import verify_checksum


class RequestServerLogin(LoginClientPacket):
    type = Int8(2)
    arg_order = ["type", "login_ok1", "login_ok2", "server_id"]

    def __init__(self, login_ok1, login_ok2, server_id):
        self.login_ok1 = Int32(login_ok1)
        self.login_ok2 = Int32(login_ok2)
        self.server_id = Int8(server_id)

    @classmethod
    @verify_checksum
    def parse(cls, data, client):
        data = ByteArray(data[1:])
        login_ok1 = data[0:4]
        login_ok2 = data[4:8]
        server_id = data[8]
        return cls(login_ok1, login_ok2, server_id)
