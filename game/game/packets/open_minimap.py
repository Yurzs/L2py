from typing import TYPE_CHECKING, ClassVar

from common.ctype import ctype
from game.packets.base import GameServerPacket

if TYPE_CHECKING:
    from game.session import GameSession


class OpenMinimap(GameServerPacket):
    type: ctype.int8 = 157
    map_id: ctype.int32
    seven_signs_period: ctype.int32
