from typing import TYPE_CHECKING, ClassVar

from common.ctype import ctype
from common.misc import extend_bytearray
from game.models.structures.object.position import Position
from game.packets.base import GameServerPacket
from game.session import GameSession

if TYPE_CHECKING:
    from game.models.character import Character


class CharMoveToLocation(GameServerPacket):
    type: ctype.int8 = 1
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
