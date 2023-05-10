from typing import ClassVar

from common.ctype import ctype

from .base import GameServerPacket


class NetPingRequest(GameServerPacket):
    type: ctype.int8 = 211
    ping_id: ctype.int32
