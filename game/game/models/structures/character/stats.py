from dataclasses import dataclass, field

from common.dataclass import BaseDataclass
from game.models.structures.character.resists import Resists


@dataclass
class BaseStats(BaseDataclass):
    str: Int32 = field(default=0)
    con: Int32 = field(default=0)
    dex: Int32 = field(default=0)
    int: Int32 = field(default=0)
    wit: Int32 = field(default=0)
    men: Int32 = field(default=0)


@dataclass
class Stats(BaseDataclass):
    max_hp: Int32 = field(default=0)
    max_mp: Int32 = field(default=0)
    max_cp: Int32 = field(default=0)
    regen_hp: Double = field(default=0)
    regen_mp: Double = field(default=0)
    regen_cp: Double = field(default=0)
    gain_mp: Double = field(default=0)
    gain_hp: Double = field(default=0)
    physical_defense: Int32 = field(default=0)
    magic_defense: Int32 = field(default=0)
    physical_attack: Int32 = field(default=0)
    magic_attack: Int32 = field(default=0)
    physical_attack_speed: Int32 = field(default=0)
    magic_attack_speed: Int32 = field(default=0)
    magic_reuse_rate: Int32 = field(default=0)
    shield_defense: Int32 = field(default=0)
    critical_damage: Int32 = field(default=0)
    pvp_physical_damage: Int32 = field(default=0)
    pvp_magic_damage: Int32 = field(default=0)
    pvp_physical_skill_damage: Int32 = field(default=0)
    accuracy: Int32 = field(default=0)
    physical_attack_range: Int32 = field(default=0)
    magic_attack_range: Int32 = field(default=0)
    physical_attack_angle: Int32 = field(default=0)
    attack_count_max: Int32 = field(default=0)
    run_speed: Int32 = field(default=0)
    walk_speed: Int32 = field(default=0)
    swim_run_speed: Int32 = field(default=0)
    swim_walk_speed: Int32 = field(default=0)
    ride_run_speed: Int32 = field(default=0)
    ride_walk_speed: Int32 = field(default=0)
    fly_run_speed: Int32 = field(default=0)
    fly_walk_speed: Int32 = field(default=0)
    base: BaseStats = BaseStats()
    resists: Resists = Resists()
    exp: Int64 = field(default=0)
    sp: Int32 = field(default=0)
    level: Int32 = field(default=1)
    evasion: Int32 = 0
    recommends_received: Int16 = field(default=0)
    recommends_left: Int8 = field(default=0)
    move_multiplier: Double = field(default=1)
    attack_speed_multiplier: Double = field(default=1)
    karma: Int32 = 0
