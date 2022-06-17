import dataclasses
import typing

from src.common.common.ctype import ctype
from src.game.game.models.structures.skill.skill import Skill

from .item import Item


@dataclasses.dataclass(kw_only=True)
class Weapon(Item):
    soulshot_count: ctype.int32
    spiritshot_count: ctype.int32
    physical_damage: ctype.int32
    random_damage: ctype.int32
    critical: ctype.int32
    hit_modifier: ctype.double
    avoid_modifier: ctype.int32
    shield_defense_rate: ctype.double
    attack_speed: ctype.int32
    attack_reuse: ctype.int32
    mp_consumption: ctype.int32
    magic_damage: ctype.int32

    passive_skill: typing.Union[None, Skill] = None
    enchant4_skill: typing.Union[None, Skill] = None

    skills_on_hit: typing.List[Skill] = ()
    skills_on_cast: typing.List[Skill] = ()
