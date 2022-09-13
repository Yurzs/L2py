from dataclasses import dataclass, field

from common.ctype import ctype
from common.misc import extend_bytearray
from game.models.character import Character
from game.packets.base import GameServerPacket


@dataclass(kw_only=True)
class FriendList(GameServerPacket):
    type: ctype.uint8 = field(default=250, init=False)
    friends: list[Character] = field(default_factory=list)

    def encode(self, session):
        encoded = bytearray()

        extend_bytearray(encoded, [self.type, ctype.int16(len(self.friends))])

        for character in self.friends:
            extend_bytearray(
                encoded,
                [
                    ctype.int16(0),  # not used, doesn't work without it
                    character.id,
                    character.name,
                    character.is_online,
                    ctype.int16(0),  # not used, doesn't work without it
                ],
            )

        return encoded
