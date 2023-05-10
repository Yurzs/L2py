from pydantic import Field

from common.ctype import ctype
from common.model import BaseModel
from game.models.structures.character.stats import Stats
from game.models.structures.object.point3d import Point3D


class LevelUpIncrease(BaseModel):
    base: ctype.float = 0
    add: ctype.float = 0
    mod: ctype.float = 0


class LevelUpGain(BaseModel):
    level: ctype.int32 = 0
    hp: LevelUpIncrease = Field(default_factory=LevelUpIncrease)
    cp: LevelUpIncrease = Field(default_factory=LevelUpIncrease)
    mp: LevelUpIncrease = Field(default_factory=LevelUpIncrease)


class ClassInfo(BaseModel):
    id: ctype.int32
    name: str
    base_level: ctype.int32


class CharacterTemplate(BaseModel):
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

    items: list[ctype.int32]

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
