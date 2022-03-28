import typing
from dataclasses import dataclass

import cython

from game.models.structures.skill.skill import Skill

from .item import Item, ItemTemplateBases, ItemTemplateDefaults


@dataclass
class ArmorBases(ItemTemplateBases):
    avoid_modifier: cython.long
    physical_defense: cython.long
    magic_defense: cython.long
    mp_bonus: cython.long
    hp_bonus: cython.long


@dataclass
class ArmorDefaults(ItemTemplateDefaults):
    passive_skill: typing.Union[None, Skill] = None


@dataclass
class Armor(Item, ArmorDefaults, ArmorBases):
    pass
