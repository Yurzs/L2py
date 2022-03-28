from .base import GameServerPacket


class QuestList(GameServerPacket):
    type = cython.char(128)
    arg_order = ["type", "quests_count"]  # TODO: custom method
