import dataclasses
import typing

from src.common.common.ctype import ctype
from src.game.game.models.structures.item.item import Item
from src.game.game.models.structures.skill.skill import Skill


@dataclasses.dataclass(kw_only=True)
class Armor(Item):
    avoid_modifier: ctype.int32 = 0
    physical_defense: ctype.int32 = 0
    magic_defense: ctype.int32 = 0
    mp_bonus: ctype.int32 = 0
    hp_bonus: ctype.int32 = 0

    passive_skill: typing.Union[None, Skill] = None
