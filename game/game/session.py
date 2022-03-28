from common.session import Session
from game.keys.xor_key import GameXorKey
from game.models.character import Character
from game.models.world import WORLD


class GameSession(Session):
    def __init__(self, protocol):
        super().__init__()

        self.id = cython.long.random()
        self.state = None
        self.protocol = protocol
        self.xor_key = GameXorKey()
        self.encryption_enabled = False
        self.session_id = None
        self.blowfish_enabled = False
        self.character = None

    def set_character(self, character: Character):
        self.character = character

    def logout_character(self):
        if self.character is not None:
            WORLD.exit(self)
            self.character = None

    def __hash__(self):
        return hash(self.uuid)
