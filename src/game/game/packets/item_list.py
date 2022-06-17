import typing
from dataclasses import dataclass, field

from src.common.common.ctype import ctype
from src.common.common.misc import extend_bytearray
from src.game.game.models.structures.item import Item
from src.game.game.packets.base import GameServerPacket


@dataclass(kw_only=True)
class ItemList(GameServerPacket):
    type: ctype.int8 = field(default=27, init=False, repr=False)

    items: typing.List[Item]
    show_window: ctype.int8 = 0

    def encode(self, session):
        encoded = bytearray(self.type)

        encoded.extend(bytes(self.show_window))
        encoded.extend(bytes(ctype.int8(len(self.items))))

        for item in self.items:
            extend_bytearray(
                encoded,
                [
                    item.type,
                    item.object_id,
                    item.id,
                    item.count,
                    item.special_type,
                    item.inventory_type,
                    item.is_equipped,
                    item.body_part,
                    item.enchant_level,
                    item.crystal_type,
                    item.augmentation,
                    item.mana,
                ],
            )

        return encoded
