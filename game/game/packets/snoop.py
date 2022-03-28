from dataclasses import dataclass, field

from game.packets.base import GameServerPacket


@dataclass
class Snoop(GameServerPacket):
    type: cython.char = field(default=213, init=False, repr=False)
    conversation_id: cython.long
    receiver: UTFString
    text_type: cython.long
    speaker: UTFString
    message: UTFString

    def encode(self, session):
        encoded = self.type.encode()

        sorted_args = [
            self.conversation_id,
            self.receiver,
            cython.long(0),
            self.text_type,
            self.speaker,
            self.message,
        ]
        for item in sorted_args:
            encoded.append(item)
        return encoded
