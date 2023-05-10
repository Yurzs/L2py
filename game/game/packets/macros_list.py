from typing import ClassVar, Optional

from common.ctype import ctype
from common.misc import extend_bytearray
from game.models.structures.macro import Macro
from game.packets.base import GameServerPacket


class MacrosList(GameServerPacket):
    type: ctype.int8 = 231
    macro: Optional[Macro] = None
    total_macros: ctype.int32 = 0
    revision: ctype.int32 = 0

    def encode(self, session):
        encoded = bytearray()

        extend_bytearray(
            encoded,
            [
                self.type,
                self.revision,
                ctype.int8(0),
                ctype.int8(self.total_macros),
                ctype.bool(self.macro),
            ],
        )

        if self.macro:
            extend_bytearray(
                encoded,
                [
                    self.macro.id,
                    self.macro.name,
                    self.macro.description,
                    self.macro.acronym,
                    self.macro.icon,
                    ctype.int8(len(self.macro.entries)),
                ],
            )
            for entry in self.macro.entries:
                extend_bytearray(
                    encoded,
                    [
                        entry.entry_id,
                        entry.type,
                        entry.skill_id,
                        entry.shortcut_id,
                        entry.command,
                    ],
                )
        return encoded
