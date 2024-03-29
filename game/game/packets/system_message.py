from typing import ClassVar

from common.ctype import ctype
from common.misc import extend_bytearray
from game.models.structures.system_message import SystemMessage
from game.packets.base import GameServerPacket


class SystemMessagePacket(GameServerPacket):
    type: ctype.int8 = 100
    message: SystemMessage

    def encode(self, session):
        encoded = bytearray(self.type)

        if not self.message:
            return encoded

        extend_bytearray(encoded, [self.message.type, ctype.int32(len(self.message.data))])

        for data in self.message.data:
            extend_bytearray(encoded, [data.type, *data.value])

        return encoded
