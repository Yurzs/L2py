import common.datatypes
from common.session import Session
from game.keys.xor_key import GameXorKey


class GameSession(Session):
    def __init__(self, protocol):
        super().__init__()

        self.id = common.datatypes.Int32.random()
        self.state = None
        self.protocol = protocol
        self.xor_key = GameXorKey()
        self.encryption_enabled = False
        self.session_id = None
        self.blowfish_enabled = False
