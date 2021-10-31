import typing
from dataclasses import dataclass, field

from game.models.structures.skill.skill import Skill

from .item import Item, ItemTemplateBases, ItemTemplateDefaults


@dataclass
class WeaponBases(ItemTemplateBases):
    soulshot_count: Int32
    spiritshot_count: Int32
    physical_damage: Int32
    random_damage: Int32
    critical: Int32
    hit_modifier: Double
    avoid_modifier: Int32
    shield_defense_rate: Double
    attack_speed: Int32
    attack_reuse: Int32
    mp_consumption: Int32
    magic_damage: Int32


@dataclass
class WeaponDefaults(ItemTemplateDefaults):
    passive_skill: typing.Union[None, Skill] = None
    enchant4_skill: typing.Union[None, Skill] = None

    skills_on_hit: typing.List[Skill] = field(default_factory=list)
    skills_on_cast: typing.List[Skill] = field(default_factory=list)


@dataclass
class Weapon(Item, WeaponDefaults, WeaponBases):
    pass
