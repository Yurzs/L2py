from typing import ClassVar

from common.ctype import ctype
from common.misc import extend_bytearray
from game.packets.base import GameServerPacket


class FriendInvite(GameServerPacket):
    type: ctype.int8 = 125
    requestor_name: str

    def encode(self, session):
        encoded = bytearray(self.type)

        extend_bytearray(encoded, [self.requestor_name])

        return encoded
