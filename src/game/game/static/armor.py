from dataclasses import dataclass, field

from src.common.common.ctype import ctype
from src.common.common.dataclass import BaseDataclass
from src.game.game.models.structures.item.item import Item, ItemProperties, ItemPropertiesBases


@dataclass(kw_only=True)
class ArmorPropertiesDefaults(BaseDataclass):
    stackable: ctype.bool = field(default=False, init=False, repr=False)


@dataclass(kw_only=True)
class ArmorPropertiesBases(ItemPropertiesBases):
    crystallizable: ctype.bool
    sellable: ctype.bool
    droppable: ctype.bool
    destroyable: ctype.bool
    tradable: ctype.bool


@dataclass(kw_only=True)
class ArmorProperties(ItemProperties, ArmorPropertiesDefaults, ArmorPropertiesBases):
    pass


class Armor(Item):
    states: ArmorProperties
    physical_defense: ctype.int32
    magic_defense: ctype.int32
    mp_bonus: ctype.int32
    armor_type: str
