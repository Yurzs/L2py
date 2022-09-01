import dataclasses

from common.ctype import ctype
from common.misc import extend_bytearray
from game.models.structures.shortcut import Shortcut
from game.packets.base import GameServerPacket


@dataclasses.dataclass(kw_only=True)
class ShortcutRegister(GameServerPacket):
    shortcut: Shortcut
    type: ctype.uint8 = 68  # 0x44

    def encode(self, session):
        encoded = bytearray()
        extend_bytearray(
            encoded,
            [
                self.type,
                ctype.int32(self.shortcut.type),  # (item=1, skill=2, action=3, macro=4, recipe=5)
                ctype.int32(self.shortcut.slot + self.shortcut.page * 12),
                ctype.int32(self.shortcut.id),
            ],
        )

        return encoded
