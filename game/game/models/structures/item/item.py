import typing
from dataclasses import dataclass, field

from common.dataclass import BaseDataclass
from common.helpers.cython import cython
from game.models.structures.object.object import L2Object, L2ObjectBases, L2ObjectDefaults
from game.models.structures.skill.skill import Skill


class Type:
    weapon_or_jewelry = 0
    shield = 1
    quest_or_adena = 4


class SpecialType:
    weapon = cython.long(0)
    shield = cython.long(1)
    accessory = cython.long(2)
    quest = cython.long(3)
    money = cython.long(4)
    other = cython.long(5)
    pet_wolf = cython.long(6)
    pet_hatchling = cython.long(7)
    pet_strider = cython.long(8)
    pet_baby = cython.long(9)


class Materials:
    steel = cython.long(0)
    fine_steel = cython.long(1)
    blood_steel = cython.long(2)
    bronze = cython.long(3)
    silver = cython.long(4)
    gold = cython.long(5)
    mithril = cython.long(6)
    oriharukon = cython.long(7)
    paper = cython.long(8)
    wood = cython.long(9)
    cloth = cython.long(10)
    leather = cython.long(11)
    bone = cython.long(12)
    damascus = cython.long(13)
    adamantaite = cython.long(14)
    chrysolite = cython.long(15)
    crystal = cython.long(16)
    liquid = cython.long(17)
    scale_of_dragon = cython.long(18)
    dyestuff = cython.long(19)
    coweb = cython.long(20)
    seed = cython.long(21)


class CrystalType:
    D = cython.long(1)
    C = cython.long(2)
    B = cython.long(3)
    A = cython.long(4)
    S = cython.long(5)


class CrystalItem:
    D = cython.long(1458)
    C = cython.long(1459)
    B = cython.long(1460)
    A = cython.long(1461)
    S = cython.long(1462)


class CrystalEnchantBonusArmor:
    D = cython.long(11)
    C = cython.long(6)
    B = cython.long(11)
    A = cython.long(19)
    S = cython.long(25)


class CrystalEnchantBonusWeapon:
    D = cython.long(90)
    C = cython.long(45)
    B = cython.long(67)
    A = cython.long(144)
    S = cython.long(250)


class Crystal:
    TYPE = CrystalType
    ITEM = CrystalItem
    BONUS_WEAPON = CrystalEnchantBonusWeapon
    BONUS_ARMOR = CrystalEnchantBonusArmor


class ItemLocation:
    VOID = 0
    INVENTORY = 1
    PAPERDOLL = 2
    WAREHOUSE = 3
    CLAN_WAREHOUSE = 4
    PET = 5
    PET_EQUIPMENT = 6
    LEASE = 7
    FREIGHT = 8


@dataclass
class ItemPropertiesBases:
    crystallizable: cython.bint
    stackable: cython.bint
    sellable: cython.bint
    droppable: cython.bint
    destroyable: cython.bint
    tradable: cython.bint
    degradable: cython.bint


@dataclass
class ItemProperties(BaseDataclass, ItemPropertiesBases):
    pass


@dataclass
class Crystallization:
    type: cython.long = 0
    count: cython.long = 0


@dataclass
class ItemTemplateBases(L2ObjectBases):
    type: cython.long
    inventory_type: cython.long
    special_type: cython.long
    weight: cython.long
    material: cython.long
    crystallization: Crystallization
    duration: cython.long
    body_part: str
    price: cython.long
    properties: ItemProperties


@dataclass
class ItemTemplateDefaults(L2ObjectDefaults):
    skills: typing.List[Skill] = field(default_factory=list)
    object_id: cython.long = field(default_factory=cython.long)


@dataclass
class ItemTemplate(L2Object, ItemTemplateDefaults, ItemTemplateBases):
    def validate_material(self):
        if self.material not in Materials.__dict__:
            raise Exception("Unknown material")


ItemTemplate.update_forward_refs()


@dataclass
class ItemDefaults(ItemTemplateDefaults):
    decrease: cython.bint = False
    augmentation: cython.long = None
    mana: cython.long = -1
    consuming_mana: cython.bint = False
    mana_consumption_rate = 60000

    charged_soulshot: cython.long = 0
    charged_spiritshot: cython.long = 0
    charged_fishshot: cython.bint = False

    last_change: cython.long = 2

    is_equipped: cython.bint = False
    enchant_level: cython.long = 0
    crystal_type: cython.char = 0


@dataclass
class ItemBases(ItemTemplateBases):
    owner_id: cython.long
    count: cython.long
    initial_count: cython.long
    usage_time: cython.long
    item_template: ItemTemplate
    location: cython.long
    slot: cython.long
    enchant: cython.long
    price_sell: cython.long
    price_buy: cython.long
    wear: cython.bint
    drop_time: cython.long
    protected: cython.bint


@dataclass
class Item(ItemTemplate, ItemDefaults, ItemBases):
    pass
