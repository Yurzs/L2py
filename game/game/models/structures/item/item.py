import dataclasses
import typing

from common.ctype import ctype
from common.dataclass import BaseDataclass
from game.models.structures.object.object import L2Object
from game.models.structures.skill.skill import Skill


class Type:
    weapon_or_jewelry = 0
    shield = 1
    quest_or_adena = 4


class SpecialType:
    weapon: ctype.int32 = 0
    shield: ctype.int32 = 1
    accessory: ctype.int32 = 2
    quest: ctype.int32 = 3
    money: ctype.int32 = 4
    other: ctype.int32 = 5
    pet_wolf: ctype.int32 = 6
    pet_hatchling: ctype.int32 = 7
    pet_strider: ctype.int32 = 8
    pet_baby: ctype.int32 = 9


class Materials:
    steel: ctype.int32 = 0
    fine_steel: ctype.int32 = 1
    blood_steel: ctype.int32 = 2
    bronze: ctype.int32 = 3
    silver: ctype.int32 = 4
    gold: ctype.int32 = 5
    mithril: ctype.int32 = 6
    oriharukon: ctype.int32 = 7
    paper: ctype.int32 = 8
    wood: ctype.int32 = 9
    cloth: ctype.int32 = 10
    leather: ctype.int32 = 11
    bone: ctype.int32 = 12
    damascus: ctype.int32 = 13
    adamantaite: ctype.int32 = 14
    chrysolite: ctype.int32 = 15
    crystal: ctype.int32 = 16
    liquid: ctype.int32 = 17
    scale_of_dragon: ctype.int32 = 18
    dyestuff: ctype.int32 = 19
    coweb: ctype.int32 = 20
    seed: ctype.int32 = 21


class CrystalType:
    D: ctype.int32 = 1
    C: ctype.int32 = 2
    B: ctype.int32 = 3
    A: ctype.int32 = 4
    S: ctype.int32 = 5


class CrystalItem:
    D: ctype.int32 = 1458
    C: ctype.int32 = 1459
    B: ctype.int32 = 1460
    A: ctype.int32 = 1461
    S: ctype.int32 = 1462


class CrystalEnchantBonusArmor:
    D: ctype.int32 = 11
    C: ctype.int32 = 6
    B: ctype.int32 = 11
    A: ctype.int32 = 19
    S: ctype.int32 = 25


class CrystalEnchantBonusWeapon:
    D: ctype.int32 = 90
    C: ctype.int32 = 45
    B: ctype.int32 = 67
    A: ctype.int32 = 144
    S: ctype.int32 = 250


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


@dataclasses.dataclass(kw_only=True)
class ItemProperties(BaseDataclass):
    crystallizable: ctype.bool
    stackable: ctype.bool
    sellable: ctype.bool
    droppable: ctype.bool
    destroyable: ctype.bool
    tradable: ctype.bool
    degradable: ctype.bool


@dataclasses.dataclass(kw_only=True)
class Crystallization:
    type: ctype.int32 = 0
    count: ctype.int32 = 0


@dataclasses.dataclass(kw_only=True)
class ItemTemplate(L2Object):
    type: ctype.int32
    inventory_type: ctype.int32
    special_type: ctype.int32
    weight: ctype.int32
    material: ctype.int32
    crystallization: Crystallization
    duration: ctype.int32
    body_part: str
    price: ctype.int32
    properties: ItemProperties

    skills: typing.List[Skill]
    object_id: ctype.int32

    def validate_material(self):
        if self.material not in Materials.__dict__:
            raise Exception("Unknown material")


@dataclasses.dataclass(kw_only=True)
class Item(ItemTemplate):
    owner_id: ctype.int32
    count: ctype.int32
    initial_count: ctype.int32
    usage_time: ctype.int32
    item_template: ItemTemplate
    location: ctype.int32
    slot: ctype.int32
    enchant: ctype.int32
    price_sell: ctype.int32
    price_buy: ctype.int32
    wear: ctype.bool
    drop_time: ctype.int32
    protected: ctype.bool

    decrease: ctype.bool = False
    augmentation: ctype.int32 = None
    mana: ctype.int32 = -1
    consuming_mana: ctype.bool = False
    mana_consumption_rate = 60000

    charged_soulshot: ctype.int32 = 0
    charged_spiritshot: ctype.int32 = 0
    charged_fishshot: ctype.bool = False

    last_change: ctype.int32 = 2

    is_equipped: ctype.bool = False
    enchant_level: ctype.int32 = 0
    crystal_type: ctype.int8 = 0
