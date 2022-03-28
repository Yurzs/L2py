from dataclasses import dataclass, field

from common.dataclass import BaseDataclass
from common.helpers.cython import cython
from game.models.structures.character.resists import Resists


@dataclass
class BaseStats(BaseDataclass):
    str: cython.long = field(default=0)
    con: cython.long = field(default=0)
    dex: cython.long = field(default=0)
    int: cython.long = field(default=0)
    wit: cython.long = field(default=0)
    men: cython.long = field(default=0)


@dataclass
class Stats(BaseDataclass):
    max_hp: cython.long = field(default=0)
    max_mp: cython.long = field(default=0)
    max_cp: cython.long = field(default=0)
    regen_hp: cython.double = field(default=0)
    regen_mp: cython.double = field(default=0)
    regen_cp: cython.double = field(default=0)
    gain_mp: cython.double = field(default=0)
    gain_hp: cython.double = field(default=0)
    physical_defense: cython.long = field(default=0)
    magic_defense: cython.long = field(default=0)
    physical_attack: cython.long = field(default=0)
    magic_attack: cython.long = field(default=0)
    physical_attack_speed: cython.long = field(default=0)
    magic_attack_speed: cython.long = field(default=0)
    magic_reuse_rate: cython.long = field(default=0)
    shield_defense: cython.long = field(default=0)
    critical_damage: cython.long = field(default=0)
    pvp_physical_damage: cython.long = field(default=0)
    pvp_magic_damage: cython.long = field(default=0)
    pvp_physical_skill_damage: cython.long = field(default=0)
    accuracy: cython.long = field(default=0)
    physical_attack_range: cython.long = field(default=0)
    magic_attack_range: cython.long = field(default=0)
    physical_attack_angle: cython.long = field(default=0)
    attack_count_max: cython.long = field(default=0)
    run_speed: cython.long = field(default=0)
    walk_speed: cython.long = field(default=0)
    swim_run_speed: cython.long = field(default=0)
    swim_walk_speed: cython.long = field(default=0)
    ride_run_speed: cython.long = field(default=0)
    ride_walk_speed: cython.long = field(default=0)
    fly_run_speed: cython.long = field(default=0)
    fly_walk_speed: cython.long = field(default=0)
    base: BaseStats = BaseStats()
    resists: Resists = Resists()
    exp: cython.longlong = field(default=0)
    sp: cython.long = field(default=0)
    level: cython.long = field(default=1)
    evasion: cython.long = 0
    recommends_received: cython.int = field(default=0)
    recommends_left: cython.char = field(default=0)
    move_multiplier: cython.double = field(default=1)
    attack_speed_multiplier: cython.double = field(default=1)
    karma: cython.long = 0
