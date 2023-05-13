from typing import ClassVar

from common.ctype import ctype
from common.misc import extend_bytearray
from game.packets.base import GameServerPacket


class CreatureSay(GameServerPacket):
    type: ctype.int8 = 74
    object_id: ctype.int32
    text_type: ctype.int32
    character_name: str
    text: str

    def encode(self, session):
        encoded = bytearray()

        extend_bytearray(
            encoded,
            [
                self.type,
                self.object_id,
                self.text_type,
                self.character_name,
                self.text,
            ],
        )

        return encoded
