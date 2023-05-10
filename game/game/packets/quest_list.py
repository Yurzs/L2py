from typing import ClassVar

from common.ctype import ctype

from .base import GameServerPacket


class QuestList(GameServerPacket):
    type: ctype.int8 = 128
    quests_count: ctype.int16 = 0
