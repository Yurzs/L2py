import dataclasses
from dataclasses import field

from src.common.common.ctype import ctype
from src.common.common.dataclass import BaseDataclass
from src.game.game.models.structures.character.stats import Stats
from src.game.game.models.structures.object.point3d import Point3D


@dataclasses.dataclass(kw_only=True)
class LevelUpIncrease(BaseDataclass):
    base: ctype.float = 0
    add: ctype.float = 0
    mod: ctype.float = 0


@dataclasses.dataclass(kw_only=True)
class LevelUpGain(BaseDataclass):
    level: ctype.int32 = 0
    hp: LevelUpIncrease = field(default_factory=LevelUpIncrease)
    cp: LevelUpIncrease = field(default_factory=LevelUpIncrease)
    mp: LevelUpIncrease = field(default_factory=LevelUpIncrease)


@dataclasses.dataclass(kw_only=True)
class ClassInfo(BaseDataclass):
    id: ctype.int32
    name: str
    base_level: ctype.int32


@dataclasses.dataclass(kw_only=True)
class CharacterTemplate(BaseDataclass):
    class_info: ClassInfo
    stats: Stats
    race: ctype.int32
    level_up_gain: LevelUpGain
    spawn: Point3D

    collision_radius: ctype.double
    collision_height: ctype.double
    load: ctype.int32

    mp_consume_rate: ctype.int32
    hp_consume_rate: ctype.int32

    items: list

    @classmethod
    def from_static_template(cls, template, sex):
        return cls(
            class_info=ClassInfo(
                id=template.class_id,
                name=template.class_name,
                base_level=template.base_level,
            ),
            stats=template.stats,
            race=template.race_id,
            level_up_gain=template.level_up_gain,
            spawn=template.spawn,
            collision_radius=template.male_collision_radius
            if sex
            else template.female_collision_radius,
            collision_height=template.male_collision_height
            if sex
            else template.female_collision_height,
            load=template.load,
            mp_consume_rate=0,
            hp_consume_rate=0,
            items=template.items,
        )
