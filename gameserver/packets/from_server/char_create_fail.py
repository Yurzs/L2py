from .base import GameServerPacket
from common.datatypes import Int8, Int32


class CharCreateFail(GameServerPacket):
    type = Int8(26)
    arg_order = ["type", "reason_id"]

    def __init__(self, reason_id):
        self.reason_id = Int32(reason_id)
