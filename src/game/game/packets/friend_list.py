import typing
from dataclasses import dataclass, field

from src.common.common.ctype import ctype
from src.game.game.models.character import Character
from src.game.game.packets.base import GameServerPacket

if typing.TYPE_CHECKING:
    from src.game.game.session import GameSession


@dataclass(kw_only=True)
class FriendList(GameServerPacket):
    type: ctype.int8 = field(default=250, init=False, repr=False)
