from .base import GameServerPacket


class ChairSit(GameServerPacket):
    type = Int8(225)
    arg_order = ["type", "object_id", "static_object_id"]

    def __init__(self, object_id, static_object_id):
        self.object_id = Int32(object_id)
        self.static_object_id = Int32(static_object_id)
