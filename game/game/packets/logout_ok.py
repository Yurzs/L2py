from typing import ClassVar

from common.ctype import ctype

from .base import GameServerPacket


class LogoutOk(GameServerPacket):
    type: ctype.int8 = 126

    def encode(self, session):
        encoded = bytearray(self.type)
        return encoded
