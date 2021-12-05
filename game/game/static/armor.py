from dataclasses import dataclass, field

from common.dataclass import BaseDataclass
from game.models.structures.item.item import Item, ItemProperties, ItemPropertiesBases


@dataclass
class ArmorPropertiesDefaults(BaseDataclass):
    stackable: Bool = field(default=False, init=False, repr=False)


@dataclass
class ArmorPropertiesBases(ItemPropertiesBases):
    crystallizable: Bool
    sellable: Bool
    droppable: Bool
    destroyable: Bool
    tradable: Bool


@dataclass
class ArmorProperties(ItemProperties, ArmorPropertiesDefaults, ArmorPropertiesBases):
    pass


class Armor(Item):
    states: ArmorProperties
    physical_defense: Int32
    magic_defense: Int32
    mp_bonus: Int32
    armor_type: UTFString
