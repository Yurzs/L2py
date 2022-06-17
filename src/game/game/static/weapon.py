import typing
from dataclasses import dataclass, field

from src.common.common.ctype import ctype
from src.common.common.dataclass import BaseDataclass


@dataclass(kw_only=True)
class Weapon(BaseDataclass):
    item_id: ctype.int32
    name: str
    bodypart: str
    crystallizable: bool
    weight: ctype.int32
    soulshots: ctype.char
    spiritshots: ctype.char
    material: str
    crystal_type: typing.Optional[str]
    physical_damage: ctype.int32
    random_damage: ctype.int32
    critical: ctype.int32
    hit_modify: ctype.int32
    avoid_modify: ctype.int32
    shield_defense: ctype.int32
    shield_defense_rate: ctype.int32
    attack_speed: ctype.int32
    mp_consume: ctype.int32
    magic_damage: ctype.int32
    duration: ctype.int32
    price: ctype.int32
    crystal_count: ctype.int32
    sellable: ctype.char
    droppable: ctype.char
    destroyable: ctype.char
    tradeable: ctype.char
    item_skill_id: ctype.int32
    item_skill_level: ctype.int32
    weapon_type: str
    on_cast_skill_id: ctype.int32
    on_cast_skill_level: ctype.int32
    on_cast_skill_chance: ctype.int32
    on_crit_skill_id: ctype.int32
    on_crit_skill_level: ctype.int32
    on_crit_skill_chance: ctype.int32
