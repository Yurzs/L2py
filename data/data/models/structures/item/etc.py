import typing
from dataclasses import dataclass, field

from data.models.structures.skill.skill import Skill

from .item import Item, ItemBases, ItemDefaults


class EtcItemType:
    ARROW = 0
    MATERIAL = 1
    PET_COLLAR = 2
    POTION = 3
    RECIPE = 4
    SCROLL = 5
    QUEST = 6
    MONEY = 7
    OTHER = 8
    SPELLBOOK = 9
    SEED = 10
    SHOT = 11
    HERB = 12


@dataclass
class EtcItem(Item):
    @property
    def is_consumable(self):
        match self.type:
            case EtcItemType.SHOT:
                return True
            case EtcItemType.POTION:
                return True
            case _:
                return False
