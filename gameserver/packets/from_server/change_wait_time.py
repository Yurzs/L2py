from .base import GameServerPacket
from common.datatypes import Int8, Int32


class ChangeWaitType(GameServerPacket):
    type = Int8(47)
    arg_order = ["type", "character_id", "wait_type", "x", "y", "z"]

    def __init__(self, character_id, wait_type, x, y, z):
        self.character_id = Int32(character_id)
        self.wait_type = Int32(wait_type)
        self.x = Int32(x)
        self.y = Int32(y)
        self.z = Int32(z)
        