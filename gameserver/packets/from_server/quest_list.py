from .base import GameServerPacket
from common.datatypes import Int8, Int32


class QuestList(GameServerPacket):
    type = Int8(128)
    arg_order = ["type", "quests_count"]  # TODO: custom method
