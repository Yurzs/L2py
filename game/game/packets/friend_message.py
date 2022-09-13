from dataclasses import dataclass, field

from common.ctype import ctype
from common.misc import extend_bytearray
from game.packets.base import GameServerPacket


@dataclass(kw_only=True)
class FriendMessage(GameServerPacket):
    type: ctype.uint8 = field(default=253, init=False)
    recipient_name: str
    sender_name: str
    message: str

    def encode(self, session):
        encoded = bytearray()

        extend_bytearray(
            encoded,
            [
                self.type,
                ctype.int32(0),   # not used, doesn't work without it
                self.recipient_name,
                self.sender_name,
                self.message
            ]
        )

        return encoded
