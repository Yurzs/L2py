import typing
from dataclasses import dataclass, field

from game.models.structures.item.item import Item
from game.packets.base import GameServerPacket


@dataclass
class ItemList(GameServerPacket):
    type: Int8 = field(default=27, init=False, repr=False)

    items: typing.List[Item]
    show_window: Bool = False

    def encode(self, session):
        encoded = self.type.encode()

        encoded.append(Int16(self.show_window))
        encoded.append(Int16(len(self.items)))

        for item in self.items:
            encoded.extend(
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
                ]
            )

        return encoded
