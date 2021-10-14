from dataclasses import dataclass, field

import common.datatypes
from common.dataclass import BaseDataclass
from data.models.structures.character.resists import Resists


@dataclass
class BaseStats(BaseDataclass):
    str: common.datatypes.Int32 = field(default=0)
    con: common.datatypes.Int32 = field(default=0)
    dex: common.datatypes.Int32 = field(default=0)
    int: common.datatypes.Int32 = field(default=0)
    wit: common.datatypes.Int32 = field(default=0)
    men: common.datatypes.Int32 = field(default=0)


@dataclass
class Stats(BaseDataclass):
    max_hp: common.datatypes.Double = field(default=0)
    max_mp: common.datatypes.Double = field(default=0)
    max_cp: common.datatypes.Double = field(default=0)
    regen_hp: common.datatypes.Double = field(default=0)
    regen_mp: common.datatypes.Double = field(default=0)
    regen_cp: common.datatypes.Double = field(default=0)
    gain_mp: common.datatypes.Double = field(default=0)
    gain_hp: common.datatypes.Double = field(default=0)
    physical_defense: common.datatypes.Int32 = field(default=0)
    magic_defense: common.datatypes.Int32 = field(default=0)
    physical_attack: common.datatypes.Int32 = field(default=0)
    magic_attack: common.datatypes.Int32 = field(default=0)
    physical_attack_speed: common.datatypes.Int32 = field(default=0)
    magic_attack_speed: common.datatypes.Int32 = field(default=0)
    magic_reuse_rate: common.datatypes.Int32 = field(default=0)
    shield_defense: common.datatypes.Int32 = field(default=0)
    critical_damage: common.datatypes.Int32 = field(default=0)
    pvp_physical_damage: common.datatypes.Int32 = field(default=0)
    pvp_magic_damage: common.datatypes.Int32 = field(default=0)
    pvp_physical_skill_damage: common.datatypes.Int32 = field(default=0)
    accuracy: common.datatypes.Int32 = field(default=0)
    physical_attack_range: common.datatypes.Int32 = field(default=0)
    magic_attack_range: common.datatypes.Int32 = field(default=0)
    physical_attack_angle: common.datatypes.Int32 = field(default=0)
    attack_count_max: common.datatypes.Int32 = field(default=0)
    run_speed: common.datatypes.Int32 = field(default=0)
    walk_speed: common.datatypes.Int32 = field(default=0)
    base: BaseStats = BaseStats()
    resists: Resists = Resists()
    exp: common.datatypes.Int64 = field(default=0)
    sp: common.datatypes.Int32 = field(default=0)
    level: common.datatypes.Int32 = field(default=0)
    evasion: common.datatypes.Int32 = 0
