import typing
from dataclasses import dataclass, field

from data.models.character import Character
from data.models.structures.object.position import Position
from game.packets.base import GameServerPacket

if typing.TYPE_CHECKING:
    from game.session import GameSession


@dataclass
class CharMoveToLocation(GameServerPacket):
    type: Int8 = field(default=1, init=False, repr=False)
    character: Character
    new_position: Position

    def encode(self, session: "GameSession"):
        encoded = self.type.encode()

        ordered_data = [
            self.character.id,
            self.new_position.point3d.x,
            self.new_position.point3d.y,
            self.new_position.point3d.z,
            self.character.position.point3d.x,
            self.character.position.point3d.y,
            self.character.position.point3d.z,
        ]
        for item in ordered_data:
            encoded.append(item)
        return encoded
