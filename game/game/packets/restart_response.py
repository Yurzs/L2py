import typing
from dataclasses import dataclass, field

from common.ctype import ctype
from common.misc import extend_bytearray
from game.packets.base import GameServerPacket

if typing.TYPE_CHECKING:
    from game.session import GameSession


@dataclass(kw_only=True)
class RestartResponse(GameServerPacket):
    type: ctype.int8 = field(default=95, init=False, repr=False)
    ok: ctype.int32 = field(default=1, init=False, repr=False)
    message: str

    def encode(self, session):
        encoded = bytearray()

        extend_bytearray(
            encoded,
            [
                self.type,
                self.ok,
                self.message,
            ],
        )

        return encoded
