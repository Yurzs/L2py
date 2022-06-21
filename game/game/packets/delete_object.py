import dataclasses

from common.ctype import ctype
from common.misc import extend_bytearray
from game.models.structures.object.object import L2Object
from game.packets.base import GameServerPacket


@dataclasses.dataclass(kw_only=True)
class DeleteObject(GameServerPacket):
    type: ctype.int8 = dataclasses.field(init=False, default=18, repr=False)
    obj: L2Object

    def encode(self, session):
        encoded = bytearray()
        extend_bytearray(
            encoded,
            [
                self.type,
                self.obj.id,
                ctype.int32(0),
            ],
        )
        return encoded
