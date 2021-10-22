from dataclasses import dataclass, field

from game.packets.base import GameServerPacket


@dataclass
class CreatureSay(GameServerPacket):
    type: Int8 = field(default=74, init=False, repr=False)
    object_id: Int32
    text_type: Int32
    character_name: UTFString
    text: UTFString
