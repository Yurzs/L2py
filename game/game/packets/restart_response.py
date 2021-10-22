import typing
from dataclasses import dataclass, field

from data.models.character import Character
from game.packets.base import GameServerPacket

if typing.TYPE_CHECKING:
    from game.session import GameSession


@dataclass
class RestartResponse(GameServerPacket):
    type: Int8 = field(default=95, init=False, repr=False)
    ok: Int32 = field(default=1, init=False, repr=False)
    message: UTFString
