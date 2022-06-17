import typing
from dataclasses import field

from src.common.common.ctype import ctype
from src.common.common.session import Session
from src.game.game.keys.xor_key import GameXorKey
from src.game.game.models.world import WORLD

if typing.TYPE_CHECKING:
    from src.game.game.models.character import Character


class GameSession(Session):
    id: ctype.int32 = field(default_factory=lambda: ctype.int32.random())

    def __init__(self, protocol):
        super().__init__()

        self.id = ctype.int32.random()
        self.state = None
        self.protocol = protocol
        self.xor_key = GameXorKey()
        self.encryption_enabled = False
        self.session_id = None
        self.blowfish_enabled = False
        self.character: Character = None

    def set_character(self, character: "Character"):
        self.character = character

    def logout_character(self):
        if self.character is not None:
            WORLD.exit(self)
            self.character = None

    def __hash__(self):
        return hash(self.uuid)
