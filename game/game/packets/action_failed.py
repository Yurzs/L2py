from common.datatypes import Int8

from .base import GameServerPacket


class ActionFailed(GameServerPacket):
    type = Int8(37)
    arg_order = ["type"]
