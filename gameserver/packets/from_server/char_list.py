from common.datatypes import Int8
from .base import GameServerPacket


class CharList(GameServerPacket):
    type = Int8(13)
