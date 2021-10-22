import typing
from dataclasses import dataclass, field

from common.dataclass import BaseDataclass


@dataclass
class Weapon(BaseDataclass):
    item_id: Int16
    name: String
    bodypart: String
    crystallizable: bool
    weight: Int16
    soulshots: Int8
    spiritshots: Int8
    material: String
    crystal_type: typing.Optional[String]
    physical_damage: Int16
    random_damage: Int16
    critical: Int16
    hit_modify: Int16
    avoid_modify: Int16
    shield_defense: Int16
    shield_defense_rate: Int16
    attack_speed: Int16
    mp_consume: Int16
    magic_damage: Int16
    duration: Int16
    price: Int16
    crystal_count: Int16
    sellable: Int8
    droppable: Int8
    destroyable: Int8
    tradeable: Int8
    item_skill_id: Int16
    item_skill_level: Int16
    weapon_type: String
    on_cast_skill_id: Int16
    on_cast_skill_level: Int16
    on_cast_skill_chance: Int16
    on_crit_skill_id: Int16
    on_crit_skill_level: Int16
    on_crit_skill_chance: Int16
