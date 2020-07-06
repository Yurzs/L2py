from .base import GameServerPacket
from common.datatypes import Int8


class ActionFailed(GameServerPacket):
    type = Int8(37)
    arg_order = ["type"]
