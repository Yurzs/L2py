from common.datatypes import Int8
from .base import GameClientPacket


class CharacterCreate(GameClientPacket):
    type = Int8(11)
