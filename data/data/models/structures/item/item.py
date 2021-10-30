import typing
from dataclasses import dataclass, field

from common.dataclass import BaseDataclass
from data.models.structures.skill.skill import Skill


class Type:
    weapon_or_jewelry = 0
    shield = 1
    quest_or_adena = 4


class SpecialType:
    weapon = Int32(0)
    shield = Int32(1)
    accessory = Int32(2)
    quest = Int32(3)
    money = Int32(4)
    other = Int32(5)
    pet_wolf = Int32(6)
    pet_hatchling = Int32(7)
    pet_strider = Int32(8)
    pet_baby = Int32(9)


class Materials:
    steel = Int32(0)
    fine_steel = Int32(1)
    blood_steel = Int32(2)
    bronze = Int32(3)
    silver = Int32(4)
    golD = Int32(5)
    mithril = Int32(6)
    oriharukon = Int32(7)
    paper = Int32(8)
    wooD = Int32(9)
    cloth = Int32(10)
    leather = Int32(11)
    bone = Int32(12)
    damascuS = Int32(13)
    adamantaite = Int32(14)
    chrysolite = Int32(15)
    crystal = Int32(16)
    liquid = Int32(17)
    scale_of_dragon = Int32(18)
    dyestuff = Int32(19)
    coweb = Int32(20)
    seed = Int32(21)


class CrystalType:
    D = Int32(1)
    C = Int32(2)
    B = Int32(3)
    A = Int32(4)
    S = Int32(5)


class CrystalItem:
    D = Int32(1458)
    C = Int32(1459)
    B = Int32(1460)
    A = Int32(1461)
    S = Int32(1462)


class CrystalEnchantBonusArmor:
    D = Int32(11)
    C = Int32(6)
    B = Int32(11)
    A = Int32(19)
    S = Int32(25)


class CrystalEnchantBonusWeapon:
    D = Int32(90)
    C = Int32(45)
    B = Int32(67)
    A = Int32(144)
    S = Int32(250)


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
    crystallizable: Bool
    stackable: Bool
    sellable: Bool
    droppable: Bool
    destroyable: Bool
    tradable: Bool
    degradable: Bool


@dataclass
class ItemProperties(BaseDataclass, ItemPropertiesBases):
    pass


@dataclass
class Crystallization:
    type: Int32 = 0
    count: Int32 = 0


@dataclass
class ItemBases(BaseDataclass):
    id: Int32
    name: UTFString
    type: Int32
    inventory_type: Int32
    special_type: Int32
    weight: Int32
    material: Int32
    crystallization: Crystallization
    duration: Int32
    body_part: UTFString
    price: Int32
    properties: ItemProperties


@dataclass
class ItemDefaults(BaseDataclass):
    skills: typing.List[Skill] = field(default_factory=list)
    object_id: Int32 = field(default_factory=Int32.random)


@dataclass
class Item(ItemDefaults, ItemBases):
    @ItemBases.post_init_hook
    def check_material(self):
        if self.material not in Materials.__dict__:
            raise Exception("Unknown material")


Item.update_forward_refs()
