import typing
from dataclasses import dataclass, field

from common.dataclass import BaseDataclass


@dataclass
class Weapon(BaseDataclass):
    item_id: cython.int
    name: String
    bodypart: String
    crystallizable: bool
    weight: cython.int
    soulshots: cython.char
    spiritshots: cython.char
    material: String
    crystal_type: typing.Optional[String]
    physical_damage: cython.int
    random_damage: cython.int
    critical: cython.int
    hit_modify: cython.int
    avoid_modify: cython.int
    shield_defense: cython.int
    shield_defense_rate: cython.int
    attack_speed: cython.int
    mp_consume: cython.int
    magic_damage: cython.int
    duration: cython.int
    price: cython.int
    crystal_count: cython.int
    sellable: cython.char
    droppable: cython.char
    destroyable: cython.char
    tradeable: cython.char
    item_skill_id: cython.int
    item_skill_level: cython.int
    weapon_type: String
    on_cast_skill_id: cython.int
    on_cast_skill_level: cython.int
    on_cast_skill_chance: cython.int
    on_crit_skill_id: cython.int
    on_crit_skill_level: cython.int
    on_crit_skill_chance: cython.int
