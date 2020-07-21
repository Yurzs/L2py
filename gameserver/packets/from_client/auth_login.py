from .base import GameClientPacket
from common.datatypes import Int8, String, Int32


class RequestAuthLogin(GameClientPacket):
    type = Int8(8)

    def __init__(self, login, play_ok1, play_ok2, login_ok1, login_ok2):
        self.login = String(login)
        self.play_ok1 = Int32(play_ok1)
        self.play_ok2 = Int32(play_ok2)
        self.login_ok1 = Int32(login_ok1)
        self.login_ok2 = Int32(login_ok2)

    @classmethod
    def parse(cls, data, client):
        login, pos = String.read(data, 1)
        play_ok1 = data[pos:pos + 4]
        play_ok2 = data[pos + 4:pos + 8]
        login_ok1 = data[pos + 8:pos + 12]
        login_ok2 = data[pos + 12:pos + 16]
        return cls(login, play_ok1, play_ok2, login_ok1, login_ok2)
