from common.datatypes import Int8
from .base import GameClientPacket


class NewCharacter(GameClientPacket):
    type = Int8(168)
    arg_order = ["type"]

    @classmethod
    def parse(cls, data, client):
        return cls()
