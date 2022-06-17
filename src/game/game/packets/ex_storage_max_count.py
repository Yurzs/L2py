import typing
from dataclasses import dataclass, field

from src.common.common.ctype import ctype
from src.common.common.misc import extend_bytearray
from src.game.game.packets.base import GameServerPacket

if typing.TYPE_CHECKING:
    from src.game.game.models.character import Character
    from src.game.game.session import GameSession


@dataclass(kw_only=True)
class ExStorageMaxCount(GameServerPacket):
    type: ctype.int8 = field(default=254, init=False, repr=False)
    character: "Character"

    def encode(self, session: "GameSession"):
        encoded = bytearray()

        extend_bytearray(
            encoded,
            [
                self.type,
                ctype.int32(0x2E),
                self.character.inventory_max,
                self.character.warehouse_max,
                self.character.freight_max,
                self.character.private_sell_max,
                self.character.private_buy_max,
                self.character.dwarf_receipt_max,
                self.character.common_receipt_max,
            ],
        )

        return encoded
