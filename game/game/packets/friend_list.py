from typing import ClassVar

from pydantic import Field

from common.ctype import ctype
from common.misc import extend_bytearray
from game.models.character import Character
from game.packets.base import GameServerPacket


class FriendList(GameServerPacket):
    type: ctype.int8 = 250
    friends: list[Character] = Field(default_factory=list)

    def encode(self, session):
        encoded = bytearray(self.type)

        if not self.friends:
            return encoded

        extend_bytearray(encoded, [ctype.int16(len(self.friends))])

        for character in self.friends:
            is_online = ctype.int32(1) if character.session else ctype.int32(0)

            extend_bytearray(
                encoded,
                [
                    ctype.int16(0),  # not used, doesn't work without it
                    character.id,
                    character.name,
                    is_online,
                    ctype.int16(0),  # not used, doesn't work without it
                ],
            )

        return encoded
