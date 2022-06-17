import typing
from dataclasses import dataclass, field

from src.common.common.ctype import ctype
from src.common.common.misc import extend_bytearray
from src.game.game.models.structures.object.position import Position
from src.game.game.packets.base import GameServerPacket

if typing.TYPE_CHECKING:
    from src.game.game.session import GameSession


@dataclass(kw_only=True)
class TargetUnselected(GameServerPacket):
    type: ctype.int8 = field(default=42, init=False, repr=False)
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
