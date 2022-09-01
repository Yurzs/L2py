import dataclasses
import typing

from common.ctype import ctype
from common.misc import extend_bytearray
from game.models.structures.macro import Macro
from game.models.structures.shortcut import Shortcut
from game.packets.base import GameServerPacket


@dataclasses.dataclass(kw_only=True)
class ShortcutsList(GameServerPacket):
    type: ctype.uint8 = 68  # 0x44
    # type: ctype.uint8 = 69  # 0x45
    shortcut: typing.Optional[Shortcut] = None

    def encode(self, session):
        encoded = bytearray()

        if self.shortcut:
            extend_bytearray(
                encoded,
                [
                    ctype.int32(self.shortcut.slot + self.shortcut.page * 12),  # slot
                    ctype.int32(
                        3
                    ),  # TODO: get values from enum (item=1, skill=2, action=3, macro=4, recipe=5)
                    ctype.int32(1),  # unknown
                ],
            )
        return encoded
