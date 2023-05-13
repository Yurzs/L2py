from typing import ClassVar

from pydantic import Field

from common.ctype import ctype

from .base import GameServerPacket


class ChangeMoveType(GameServerPacket):
    type: ctype.int8 = 46

    character_id: ctype.int32
    move_type: ctype.int32
    constant: ctype.int32 = Field(default=0, const=True)
