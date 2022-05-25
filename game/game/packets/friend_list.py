import typing
from dataclasses import dataclass, field

from common.ctype import ctype
from game.models.character import Character
from game.packets.base import GameServerPacket

if typing.TYPE_CHECKING:
    from game.session import GameSession


@dataclass(kw_only=True)
class FriendList(GameServerPacket):
    type: ctype.int8 = field(default=250, init=False, repr=False)
