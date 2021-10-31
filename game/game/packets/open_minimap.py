import typing
from dataclasses import dataclass, field

from game.models.character import Character
from game.packets.base import GameServerPacket

if typing.TYPE_CHECKING:
    from game.session import GameSession


@dataclass
class OpenMinimap(GameServerPacket):
    type: Int8 = field(default=157, init=False, repr=False)
    map_id: Int32
    seven_signs_period: Int32
