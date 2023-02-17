from dataclasses import dataclass, field

from common.ctype import ctype
from common.misc import extend_bytearray
from game.packets.base import GameServerPacket


@dataclass(kw_only=True)
class FriendInvite(GameServerPacket):
    type: ctype.uint8 = field(default=125, init=False)
    requestor_name: str

    def encode(self, session):
        encoded = bytearray(self.type)

        extend_bytearray(encoded, [self.requestor_name])

        return encoded
