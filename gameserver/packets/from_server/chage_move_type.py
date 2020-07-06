from .base import GameServerPacket
from common.datatypes import Int32, Int8


class ChangeMoveType(GameServerPacket):
    type = Int8(62)
    arg_order = ["character_id", "move_type", "constant"]

    def __init__(self, character_id, move_type):
        self.character_id = Int32(character_id)
        self.move_type = Int32(move_type)
        self.constant = Int32(0)
