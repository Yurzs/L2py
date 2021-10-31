from dataclasses import dataclass, field

from common.dataclass import BaseDataclass


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


example = {
    "item_id": 9208,
    "name": "Phantom Mask (Event)",
    "bodypart": "dhair",
    "crystallizable": false,
    "armor_type": null,
    "weight": 10,
    "material": "wood",
    "crystal_type": null,
    "avoid_modify": 0,
    "duration": -1,
    "p_def": 0,
    "m_def": 0,
    "mp_bonus": 0,
    "price": 0,
    "crystal_count": 0,
    "sellable": false,
    "dropable": false,
    "destroyable": true,
    "tradable": false,
    "item_skill_id": 0,
    "item_skill_lvl": 0,
}


class Armor(Item):
    states: ArmorProperties
    physical_defense: Int32
    magic_defense: Int32
    mp_bonus: Int32
    armor_type: UTFString
