from .base import GameServerPacket
from common.datatypes import Int32, Int8


class CharList(GameServerPacket):
    type = Int8(13)
