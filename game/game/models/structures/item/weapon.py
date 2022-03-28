import typing
from dataclasses import dataclass, field

from game.models.structures.skill.skill import Skill

from .item import Item, ItemTemplateBases, ItemTemplateDefaults


@dataclass
class WeaponBases(ItemTemplateBases):
    soulshot_count: cython.long
    spiritshot_count: cython.long
    physical_damage: cython.long
    random_damage: cython.long
    critical: cython.long
    hit_modifier: cython.double
    avoid_modifier: cython.long
    shield_defense_rate: cython.double
    attack_speed: cython.long
    attack_reuse: cython.long
    mp_consumption: cython.long
    magic_damage: cython.long


@dataclass
class WeaponDefaults(ItemTemplateDefaults):
    passive_skill: typing.Union[None, Skill] = None
    enchant4_skill: typing.Union[None, Skill] = None

    skills_on_hit: typing.List[Skill] = field(default_factory=list)
    skills_on_cast: typing.List[Skill] = field(default_factory=list)


@dataclass
class Weapon(Item, WeaponDefaults, WeaponBases):
    pass
