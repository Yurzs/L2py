import typing
from dataclasses import field

from common.ctype import ctype
from common.session import Session
from game.keys.xor_key import GameXorKey
from game.models.world import WORLD

if typing.TYPE_CHECKING:
    from game.models.character import Character


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
