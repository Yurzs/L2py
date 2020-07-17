from common.datatypes import Int8, Int32
from .base import LoginServerPacket


class PlayOk(LoginServerPacket):
    type = Int8(7)
    arg_order = ["type", "play_ok1", "play_ok2", "unknown"]

    def __init__(self, play_ok1, play_ok2):
        self.play_ok1 = Int32(play_ok1)
        self.play_ok2 = Int32(play_ok2)
        self.unknown = Int8(1)
