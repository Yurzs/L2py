import typing
from dataclasses import dataclass, field

from src.common.common.ctype import ctype
from src.common.common.misc import extend_bytearray
from src.game.game.packets.base import GameServerPacket

if typing.TYPE_CHECKING:
    from src.game.game.session import GameSession


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
