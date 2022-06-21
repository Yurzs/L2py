import dataclasses
import typing

from common.ctype import ctype
from common.dataclass import BaseDataclass
from game.models.structures.skill.skill import Skill


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
    D = ctype.int32(1)
    C = ctype.int32(2)
    B = ctype.int32(3)
    A = ctype.int32(4)
    S = ctype.int32(5)


class CrystalItem:
    D = ctype.int32(1458)
    C = ctype.int32(1459)
    B = ctype.int32(1460)
    A = ctype.int32(1461)
    S = ctype.int32(1462)


class CrystalEnchantBonusArmor:
    D = ctype.int32(11)
    C = ctype.int32(6)
    B = ctype.int32(11)
    A = ctype.int32(19)
    S = ctype.int32(25)


class CrystalEnchantBonusWeapon:
    D = ctype.int32(90)
    C = ctype.int32(45)
    B = ctype.int32(67)
    A = ctype.int32(144)
    S = ctype.int32(250)


class Crystal:
    TYPE = CrystalType
    ITEM = CrystalItem
    BONUS_WEAPON = CrystalEnchantBonusWeapon
    BONUS_ARMOR = CrystalEnchantBonusArmor


@dataclasses.dataclass(kw_only=True)
class ItemProperties(BaseDataclass):
    crystallizable: ctype.bool = False
    stackable: ctype.bool = False
    sellable: ctype.bool = False
    droppable: ctype.bool = False
    destroyable: ctype.bool = False
    tradable: ctype.bool = False
    degradable: ctype.bool = False


@dataclasses.dataclass(kw_only=True)
class Crystallization(BaseDataclass):
    type: ctype.int32 | None = 0
    count: ctype.int32 = 0


@dataclasses.dataclass(kw_only=True)
class Item(BaseDataclass):
    id: ctype.int32
    name: str
    type: typing.Union[str, None]
    inventory_type: typing.Optional[str]
    special_type: typing.Optional[str]
    weight: ctype.int32
    material: str
    crystallization: Crystallization
    duration: ctype.int32
    body_part: typing.Optional[str]
    price: ctype.int32
    properties: ItemProperties

    skills: typing.List[Skill] = dataclasses.field(default_factory=list)

    def validate_material(self):
        if self.material not in Materials.__dict__:
            raise Exception("Unknown material")
