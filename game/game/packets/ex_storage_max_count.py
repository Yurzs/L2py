import typing
from dataclasses import dataclass, field

from game.models.character import Character
from game.packets.base import GameServerPacket

if typing.TYPE_CHECKING:
    from game.session import GameSession


@dataclass
class ExStorageMaxCount(GameServerPacket):
    type: Int8 = field(default=254, init=False, repr=False)
    character: Character

    def encode(self, session: "GameSession"):
        encoded = self.type.encode()
        encoded.append(Int16(0x2E))

        ordered_data = [
            self.character.inventory_max,
            self.character.warehouse_max,
            self.character.freight_max,
            self.character.private_sell_max,
            self.character.private_buy_max,
            self.character.dwarf_receipt_max,
            self.character.common_receipt_max,
        ]
        for item in ordered_data:
            encoded.append(item)
        return encoded
