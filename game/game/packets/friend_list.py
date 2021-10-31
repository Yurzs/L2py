import typing
from dataclasses import dataclass, field

from game.models.character import Character
from game.packets.base import GameServerPacket

if typing.TYPE_CHECKING:
    from game.session import GameSession


@dataclass
class FriendList(GameServerPacket):
    type: Int8 = field(default=250, init=False, repr=False)
