import dataclasses

from src.common.common.ctype import ctype

from .base import GameServerPacket


@dataclasses.dataclass(kw_only=True)
class MoveToLocation(GameServerPacket):
    type: ctype.int8 = 1
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
        self.object_id = ctype.int32(object_id)
        self.destination_x = ctype.int32(destination_x)
        self.destination_y = ctype.int32(destination_y)
        self.destination_z = ctype.int32(destination_z)
        self.current_x = ctype.int32(current_x)
        self.current_y = ctype.int32(current_y)
        self.current_z = ctype.int32(current_z)
