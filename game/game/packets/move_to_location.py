from common.datatypes import Int8, Int32

from .base import GameServerPacket


class MoveToLocation(GameServerPacket):
    type = Int8(1)
    arg_order = [
        "type",
        "object_id",
        "destination_x",
        "destination_y",
        "destination_z",
        "current_x",
        "current_y",
        "current_z",
    ]

    def __init__(
        self,
        object_id,
        destination_x,
        destination_y,
        destination_z,
        current_x,
        current_y,
        current_z,
    ):
        self.object_id = Int32(object_id)
        self.destination_x = Int32(destination_x)
        self.destination_y = Int32(destination_y)
        self.destination_z = Int32(destination_z)
        self.current_x = Int32(current_x)
        self.current_y = Int32(current_y)
        self.current_z = Int32(current_z)
