from typing import ClassVar, Optional

from pydantic import Field, validator

from common.ctype import ctype
from common.model import BaseModel
from game.models.structures.skill.skill import Skill


class Materials(BaseModel):
    steel: ClassVar[ctype.int32] = 0
    fine_steel: ClassVar[ctype.int32] = 1
    blood_steel: ClassVar[ctype.int32] = 2
    bronze: ClassVar[ctype.int32] = 3
    silver: ClassVar[ctype.int32] = 4
    gold: ClassVar[ctype.int32] = 5
    mithril: ClassVar[ctype.int32] = 6
    oriharukon: ClassVar[ctype.int32] = 7
    paper: ClassVar[ctype.int32] = 8
    wood: ClassVar[ctype.int32] = 9
    cloth: ClassVar[ctype.int32] = 10
    leather: ClassVar[ctype.int32] = 11
    bone: ClassVar[ctype.int32] = 12
    damascus: ClassVar[ctype.int32] = 13
    adamantaite: ClassVar[ctype.int32] = 14
    chrysolite: ClassVar[ctype.int32] = 15
    crystal: ClassVar[ctype.int32] = 16
    liquid: ClassVar[ctype.int32] = 17
    scale_of_dragon: ClassVar[ctype.int32] = 18
    dyestuff: ClassVar[ctype.int32] = 19
    coweb: ClassVar[ctype.int32] = 20
    seed: ClassVar[ctype.int32] = 21


class CrystalType(BaseModel):
    D: ClassVar[ctype.int32] = 1
    C: ClassVar[ctype.int32] = 2
    B: ClassVar[ctype.int32] = 3
    A: ClassVar[ctype.int32] = 4
    S: ClassVar[ctype.int32] = 5


class CrystalItem:
    D: ClassVar[ctype.int32] = 1458
    C: ClassVar[ctype.int32] = 1459
    B: ClassVar[ctype.int32] = 1460
    A: ClassVar[ctype.int32] = 1461
    S: ClassVar[ctype.int32] = 1462


class CrystalEnchantBonusArmor:
    D: ClassVar[ctype.int32] = 11
    C: ClassVar[ctype.int32] = 6
    B: ClassVar[ctype.int32] = 11
    A: ClassVar[ctype.int32] = 19
    S: ClassVar[ctype.int32] = 25


class CrystalEnchantBonusWeapon:
    D: ClassVar[ctype.int32] = 90
    C: ClassVar[ctype.int32] = 45
    B: ClassVar[ctype.int32] = 67
    A: ClassVar[ctype.int32] = 144
    S: ClassVar[ctype.int32] = 250


class Crystal:
    TYPE = CrystalType
    ITEM = CrystalItem
    BONUS_WEAPON = CrystalEnchantBonusWeapon
    BONUS_ARMOR = CrystalEnchantBonusArmor


class ItemProperties(BaseModel):
    crystallizable: ctype.bool = False
    stackable: ctype.bool = False
    sellable: ctype.bool = False
    droppable: ctype.bool = False
    destroyable: ctype.bool = False
    tradable: ctype.bool = False
    degradable: ctype.bool = False


class Crystallization(BaseModel):
    type: ctype.int32 | None = 0
    count: ctype.int32 = 0


class Item(BaseModel):
    id: ctype.int32
    name: str
    type: str | None
    inventory_type: Optional[str]
    special_type: Optional[str]
    weight: ctype.int32
    material: str
    crystallization: Crystallization
    duration: ctype.int32
    body_part: Optional[str]
    price: ctype.int32
    properties: ItemProperties

    skills: list[Skill] = Field(default_factory=list)

    @classmethod
    @validator("material")
    def validate_material(cls, v):
        if v not in dir(Materials):
            raise Exception("Unknown material")
        return v
