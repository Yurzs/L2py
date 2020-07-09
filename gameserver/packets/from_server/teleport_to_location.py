from common.datatypes import Int32, Int8
from .base import GameServerPacket


class TeleportToLocation(GameServerPacket):
    type = Int8(56)
    arg_order = ["type", "character_id", "x", "y", "z"]

    def __init__(self, character_id, x, y, z):
        self.character_id = Int32(character_id)
        self.x = Int32(x)
        self.y = Int32(y)
        self.z = Int32(z)
