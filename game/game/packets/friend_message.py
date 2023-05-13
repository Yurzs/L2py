from typing import ClassVar

from common.ctype import ctype
from common.misc import extend_bytearray
from game.packets.base import GameServerPacket


class FriendMessage(GameServerPacket):
    type: ctype.int8 = 253
    recipient_name: str
    sender_name: str
    message: str

    def encode(self, session):
        encoded = bytearray(self.type)

        extend_bytearray(
            encoded,
            [
                ctype.int32(0),  # not used, doesn't work without it
                self.recipient_name,
                self.sender_name,
                self.message,
            ],
        )

        return encoded
