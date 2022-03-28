from dataclasses import dataclass, field

from common.dataclass import BaseDataclass
from game.models.structures.item.item import Item, ItemProperties, ItemPropertiesBases


@dataclass
class ArmorPropertiesDefaults(BaseDataclass):
    stackable: cython.bint = field(default=False, init=False, repr=False)


@dataclass
class ArmorPropertiesBases(ItemPropertiesBases):
    crystallizable: cython.bint
    sellable: cython.bint
    droppable: cython.bint
    destroyable: cython.bint
    tradable: cython.bint


@dataclass
class ArmorProperties(ItemProperties, ArmorPropertiesDefaults, ArmorPropertiesBases):
    pass


class Armor(Item):
    states: ArmorProperties
    physical_defense: cython.long
    magic_defense: cython.long
    mp_bonus: cython.long
    armor_type: UTFString
