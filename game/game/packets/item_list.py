from typing import ClassVar

from common.ctype import ctype
from common.misc import extend_bytearray
from game.models.structures.item import Item
from game.packets.base import GameServerPacket


class ItemList(GameServerPacket):
    type: ctype.int8 = 27

    items: list[Item]
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
