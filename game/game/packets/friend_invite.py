import dataclasses

from common.ctype import ctype
from common.misc import extend_bytearray
from game.packets.base import GameServerPacket


@dataclasses.dataclass(kw_only=True)
class FriendInvite(GameServerPacket):
    requestor_name: str
    type: ctype.uint8 = 125

    def encode(self, session):
        encoded = bytearray()

        if self.requestor_name:
            extend_bytearray(encoded, [self.type, self.requestor_name])

        return encoded
