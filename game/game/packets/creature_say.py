from dataclasses import dataclass, field

from game.packets.base import GameServerPacket


@dataclass
class CreatureSay(GameServerPacket):
    type: cython.char = field(default=74, init=False, repr=False)
    object_id: cython.long
    text_type: cython.long
    character_name: UTFString
    text: UTFString
