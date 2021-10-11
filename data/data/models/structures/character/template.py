import typing
from dataclasses import dataclass, field

import common.datatypes
from common.dataclass import BaseDataclass
from data.models.structures.character.stats import Stats
from data.models.structures.item.item import Item
from data.models.structures.object.point3d import Point3D


@dataclass
class LevelUpIncrease(BaseDataclass):
    hp_add: common.datatypes.Float = 1
    hp_mod: common.datatypes.Float = 1
    cp_add: common.datatypes.Float = 1
    cp_mod: common.datatypes.Float = 1
    mp_add: common.datatypes.Float = 1
    mp_mod: common.datatypes.Float = 1


@dataclass
class ClassInfo(BaseDataclass):
    id: common.datatypes.Int8 = 1
    name: common.datatypes.UTFString = "Human Fighter"
    base_level: common.datatypes.Int32 = 1


@dataclass
class CharacterBaseTemplate(BaseDataclass):
    stats: Stats = Stats()
    is_undead: common.datatypes.Bool = False

    mp_consume_rate: common.datatypes.Int32 = 0
    hp_consume_rate: common.datatypes.Int32 = 0

    collision_radius: common.datatypes.Int32 = 0
    collision_height: common.datatypes.Int32 = 0


@dataclass
class CharacterTemplate(CharacterBaseTemplate):
    class_info: ClassInfo = ClassInfo()
    race: common.datatypes.Int8 = 1
    spawn: Point3D = Point3D()
    level_up_increase: LevelUpIncrease = LevelUpIncrease()
    items: typing.List[Item] = field(default_factory=list)
