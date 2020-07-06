import logging
from .base import LoginClientPacket
from common.utils.xor import xor_decrypt_login
from common.utils.checksum import verify_checksum
from common.datatypes.integer import Int8, Int32

log = logging.getLogger("login_server." + __name__)


class RequestGGAuth(LoginClientPacket):
    type = Int8(7)
    arg_order = ["session_id", "unknown1", "unknown2", "unknown3", "unknown4"]

    def __init__(self, session_id, unknown1, unknown2, unknown3, unknown4):
        self.session_id = Int32(session_id)
        self.unknown1 = Int32(unknown1)
        self.unknown2 = Int32(unknown2)
        self.unknown3 = Int32(unknown3)
        self.unknown4 = Int32(unknown4)

    @classmethod
    # @xor_decrypt_login
    # @verify_checksum
    def parse(cls, data, client):
        data = data[1:]
        if client.session_id != Int32(data[0:4]):
            log.error("Session_id doesnt match")
            return
        return cls(data[1:4], data[4:8], data[8:12], data[12:16], data[16:20])
