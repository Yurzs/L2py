from typing import ClassVar

from common.ctype import ctype
from common.misc import extend_bytearray
from game.packets.base import GameServerPacket


class RestartResponse(GameServerPacket):
    type: ctype.int8 = 95
    ok: ctype.int32 = 0
    message: str

    def encode(self, session):
        encoded = bytearray()

        extend_bytearray(
            encoded,
            [
                self.type,
                self.ok,
                self.message,
            ],
        )

        return encoded
