from typing import ClassVar

from common.ctype import ctype
from game.packets.base import GameServerPacket


class Snoop(GameServerPacket):
    type: ctype.int8 = 213
    conversation_id: ctype.int32
    receiver: str
    unknown_constant: ctype.int32 = 0
    text_type: ctype.int32
    speaker: str
    message: str
