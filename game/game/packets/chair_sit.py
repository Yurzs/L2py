import dataclasses

from common.ctype import ctype

from .base import GameServerPacket


@dataclasses.dataclass(kw_only=True)
class ChairSit(GameServerPacket):
    type: ctype.int8 = 225
    arg_order = ["type", "object_id", "static_object_id"]

    def __init__(self, object_id, static_object_id):
        self.object_id = ctype.int32(object_id)
        self.static_object_id = ctype.int32(static_object_id)
