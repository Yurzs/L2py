import typing
from dataclasses import dataclass, field

from src.common.common.ctype import ctype
from src.game.game.packets.base import GameServerPacket

if typing.TYPE_CHECKING:
    from src.game.game.session import GameSession


@dataclass(kw_only=True)
class OpenMinimap(GameServerPacket):
    type: ctype.int8 = field(default=157, init=False, repr=False)
    map_id: ctype.int32
    seven_signs_period: ctype.int32
