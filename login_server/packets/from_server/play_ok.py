from .base import LoginServerPacket
from common.datatypes import Int8, Int32


class PlayOk(LoginServerPacket):
    type = Int8(7)
    arg_order = ["type", "session_id2_1", "session_id2_2"]

    def __init__(self, session_id2_1, session_id2_2):
        self.session_id2_1 = Int32(session_id2_1)
        self.session_id2_2 = Int32(session_id2_2)

