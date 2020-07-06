from .base import GameServerPacket
from common.datatypes import Int8, Int32


class AuthLoginFail(GameServerPacket):
    type = Int8(12)
    arg_order = ["type", "reason_id"]

    def __init__(self, reason_id):
        self.reason_id = Int32(reason_id)
