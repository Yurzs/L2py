from typing import TYPE_CHECKING, ClassVar

from common.ctype import ctype
from common.misc import extend_bytearray
from game.models.structures.object.position import Position
from game.packets.base import GameServerPacket

if TYPE_CHECKING:
    from game.session import GameSession


class TargetUnselected(GameServerPacket):
    type: ctype.int8 = 42
    target_id: ctype.int32
    position: Position

    def encode(self, session: "GameSession"):
        encoded = bytearray()

        extend_bytearray(
            encoded,
            [
                self.type,
                self.target_id,
                self.position.point3d.x,
                self.position.point3d.y,
                self.position.point3d.z,
            ],
        )
        return encoded
