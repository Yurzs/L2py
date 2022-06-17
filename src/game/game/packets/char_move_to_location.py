import typing
from dataclasses import dataclass, field

from src.common.common.ctype import ctype
from src.common.common.misc import extend_bytearray
from src.game.game.models.structures.object.position import Position
from src.game.game.packets.base import GameServerPacket
from src.game.game.session import GameSession

if typing.TYPE_CHECKING:
    from src.game.game.models.character import Character


@dataclass(kw_only=True)
class CharMoveToLocation(GameServerPacket):
    type: ctype.int8 = field(default=1, init=False, repr=False)
    character: "Character"
    new_position: Position

    def encode(self, session: GameSession):
        encoded = bytearray()

        extend_bytearray(
            encoded,
            [
                self.type,
                self.character.id,
                self.new_position.point3d.x,
                self.new_position.point3d.y,
                self.new_position.point3d.z,
                self.character.position.point3d.x,
                self.character.position.point3d.y,
                self.character.position.point3d.z,
            ],
        )
        return encoded
