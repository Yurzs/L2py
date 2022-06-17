import dataclasses
from dataclasses import field

from src.common.common.ctype import ctype
from src.common.common.dataclass import BaseDataclass
from src.game.game.models.structures.character.resists import Resists


@dataclasses.dataclass(kw_only=True)
class BaseStats(BaseDataclass):
    STR: ctype.int32 = 0
    CON: ctype.int32 = 0
    DEX: ctype.int32 = 0
    INT: ctype.int32 = 0
    WIT: ctype.int32 = 0
    MEN: ctype.int32 = 0


@dataclasses.dataclass(kw_only=True)
class Stats(BaseDataclass):
    max_hp: ctype.int32 = 0
    max_mp: ctype.int32 = 0
    max_cp: ctype.int32 = 0
    regen_hp: ctype.float = 0.0
    regen_mp: ctype.float = 0.0
    regen_cp: ctype.float = 0.0
    gain_mp: ctype.float = 0.0
    gain_hp: ctype.float = 0.0
    physical_defense: ctype.int32 = 0
    magic_defense: ctype.int32 = 0
    physical_attack: ctype.int32 = 0
    magic_attack: ctype.int32 = 0
    physical_attack_speed: ctype.int32 = 0
    magic_attack_speed: ctype.int32 = 0
    magic_reuse_rate: ctype.int32 = 0
    shield_defense: ctype.int32 = 0
    critical_damage: ctype.int32 = 0
    pvp_physical_damage: ctype.int32 = 0
    pvp_magic_damage: ctype.int32 = 0
    pvp_physical_skill_damage: ctype.int32 = 0
    accuracy: ctype.int32 = 0
    physical_attack_range: ctype.int32 = 0
    magic_attack_range: ctype.int32 = 0
    physical_attack_angle: ctype.int32 = 0
    attack_count_max: ctype.int32 = 0
    run_speed: ctype.int32 = 70
    walk_speed: ctype.int32 = 150
    swim_run_speed: ctype.int32 = 0
    swim_walk_speed: ctype.int32 = 0
    ride_run_speed: ctype.int32 = 0
    ride_walk_speed: ctype.int32 = 0
    fly_run_speed: ctype.int32 = 0
    fly_walk_speed: ctype.int32 = 0
    base: BaseStats = field(default_factory=BaseStats)
    resists: Resists = field(default_factory=Resists)
    exp: ctype.int64 = 0
    sp: ctype.int32 = 0
    level: ctype.int32 = 0
    evasion: ctype.int32 = 0
    recommends_received: ctype.int16 = 0
    recommends_left: ctype.int16 = 0
    move_multiplier: ctype.double = 1.0
    attack_speed_multiplier: ctype.double = 1.0
    karma: ctype.int32 = 0
