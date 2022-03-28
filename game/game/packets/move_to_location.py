from .base import GameServerPacket


class MoveToLocation(GameServerPacket):
    type = cython.char(1)
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
        self.object_id = cython.long(object_id)
        self.destination_x = cython.long(destination_x)
        self.destination_y = cython.long(destination_y)
        self.destination_z = cython.long(destination_z)
        self.current_x = cython.long(current_x)
        self.current_y = cython.long(current_y)
        self.current_z = cython.long(current_z)
