import dataclasses

from common.ctype import ctype

from .base import GameServerPacket


@dataclasses.dataclass(kw_only=True)
class ExSendManorList(GameServerPacket):
    type: ctype.int8 = 254
    arg_order = ["type", "constant", ""]  # TODO custom method
    constant: ctype.int8 = 27
