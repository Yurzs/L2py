from common.ctype import ctype
from game.models.structures.item.item import Item, ItemProperties


class ArmorProperties(ItemProperties):
    stackable: ctype.bool = False
    crystallizable: ctype.bool
    sellable: ctype.bool
    droppable: ctype.bool
    destroyable: ctype.bool
    tradable: ctype.bool


class Armor(Item):
    states: ArmorProperties
    physical_defense: ctype.int32
    magic_defense: ctype.int32
    mp_bonus: ctype.int32
    armor_type: str
