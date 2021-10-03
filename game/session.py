from common.datatypes import Int32
from common.session import Session
from game.keys.xor_key import GameXorKey


class GameSession(Session):
    def __init__(self, protocol):
        super().__init__()

        self.state = None
        self.protocol = protocol
        self.xor_key = GameXorKey()
        self.encryption_enabled = False
        self.session_id = None
        self.blowfish_enabled = False
