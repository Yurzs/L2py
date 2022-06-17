import dataclasses
import typing

from src.common.common.ctype import ctype
from src.common.common.misc import extend_bytearray
from src.game.game.models.structures.macro import Macro
from src.game.game.packets.base import GameServerPacket


@dataclasses.dataclass(kw_only=True)
class MacrosList(GameServerPacket):
    type: ctype.uint8 = 231
    macro: typing.Optional[Macro] = None
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
