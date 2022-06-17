from dataclasses import dataclass, field

from src.common.common.ctype import ctype
from src.common.common.misc import extend_bytearray
from src.game.game.packets.base import GameServerPacket


@dataclass(kw_only=True)
class CreatureSay(GameServerPacket):
    type: ctype.int8 = field(default=74, init=False, repr=False)
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
