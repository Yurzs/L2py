from typing import TYPE_CHECKING, ClassVar

from common.ctype import ctype
from common.misc import extend_bytearray
from game.packets.base import GameServerPacket

if TYPE_CHECKING:
    from game.models.character import Character
    from game.session import GameSession


class ExStorageMaxCount(GameServerPacket):
    type: ctype.int8 = 254
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
