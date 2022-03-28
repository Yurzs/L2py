import typing
from dataclasses import dataclass, field

from game.models.character import Character
from game.packets.base import GameServerPacket

if typing.TYPE_CHECKING:
    from game.session import GameSession


@dataclass
class OpenMinimap(GameServerPacket):
    type: cython.char = field(default=157, init=False, repr=False)
    map_id: cython.long
    seven_signs_period: cython.long
