from common.datatypes import Int32, Int8
from .base import GameServerPacket


class AuthLoginFail(GameServerPacket):
    type = Int8(12)
    arg_order = ["type", "reason_id"]

    def __init__(self, reason_id):
        self.reason_id = Int32(reason_id)
