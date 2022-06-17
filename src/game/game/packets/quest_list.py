from src.common.common.ctype import ctype

from .base import GameServerPacket


class QuestList(GameServerPacket):
    type: ctype.int8 = 128
    arg_order = ["type", "quests_count"]  # TODO: custom method
