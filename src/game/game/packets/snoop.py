from dataclasses import dataclass, field

from src.common.common.ctype import ctype
from src.game.game.packets.base import GameServerPacket


@dataclass(kw_only=True)
class Snoop(GameServerPacket):
    type: ctype.int8 = field(default=213, init=False, repr=False)
    conversation_id: ctype.int32
    receiver: str
    text_type: ctype.int32
    speaker: str
    message: str

    def encode(self, session):
        encoded = self.type.encode()

        sorted_args = [
            self.conversation_id,
            self.receiver,
            ctype.int32(0),
            self.text_type,
            self.speaker,
            self.message,
        ]
        for item in sorted_args:
            encoded.append(item)
        return encoded
