from dataclasses import dataclass, field

from game.packets.base import GameServerPacket


@dataclass
class Snoop(GameServerPacket):
    type: Int8 = field(default=213, init=False, repr=False)
    conversation_id: Int32
    receiver: UTFString
    text_type: Int32
    speaker: UTFString
    message: UTFString

    def encode(self, session):
        encoded = self.type.encode()

        sorted_args = [
            self.conversation_id,
            self.receiver,
            Int32(0),
            self.text_type,
            self.speaker,
            self.message,
        ]
        for item in sorted_args:
            encoded.append(item)
        return encoded
