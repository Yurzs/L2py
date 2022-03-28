from common.helpers.cython import cython

from .base import GameServerPacket


class ChairSit(GameServerPacket):
    type = cython.char(225)
    arg_order = ["type", "object_id", "static_object_id"]

    def __init__(self, object_id, static_object_id):
        self.object_id = cython.long(object_id)
        self.static_object_id = cython.long(static_object_id)
