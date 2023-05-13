from typing import TYPE_CHECKING, ClassVar

from common.ctype import ctype
from common.misc import extend_bytearray
from game.packets.base import GameServerPacket

if TYPE_CHECKING:
    from game.models.character import Character
    from game.session import GameSession


class EtcStatusUpdate(GameServerPacket):
    type: ctype.int8 = 243
    character: "Character"

    def encode(self, session: "GameSession"):
        encoded = bytearray()

        extend_bytearray(
            encoded,
            [
                self.type,
                self.character.weight_penalty,
                ctype.int32(0),
                ctype.int32(0),
                self.character.exp_penalty,
                self.character.exp_protected,
                self.character.death_penalty,
            ],
        )
        return encoded
