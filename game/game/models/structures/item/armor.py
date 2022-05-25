import dataclasses
import typing

from common.ctype import ctype
from game.models.structures.item.item import Item
from game.models.structures.skill.skill import Skill


@dataclasses.dataclass(kw_only=True)
class Armor(Item):
    avoid_modifier: ctype.int32 = 0
    physical_defense: ctype.int32 = 0
    magic_defense: ctype.int32 = 0
    mp_bonus: ctype.int32 = 0
    hp_bonus: ctype.int32 = 0

    passive_skill: typing.Union[None, Skill] = None
