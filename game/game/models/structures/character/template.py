from __future__ import annotations

import typing
from dataclasses import dataclass, field

import game.static.character_template
from common.dataclass import BaseDataclass
from common.helpers.cython import cython
from game.models.structures.character.stats import Stats

# from game.models.structures.item.item import Item
from game.models.structures.object.point3d import Point3D


@dataclass
class LevelUpIncrease(BaseDataclass):
    base: cython.float
    add: cython.float
    mod: cython.float


LevelUpIncrease.update_forward_refs()


@dataclass
class LevelUpGain(BaseDataclass):
    level: cython.long
    hp: LevelUpIncrease
    cp: LevelUpIncrease
    mp: LevelUpIncrease


LevelUpGain.update_forward_refs()


@dataclass
class ClassInfo(BaseDataclass):
    id: cython.char
    name: str
    base_level: cython.long


ClassInfo.update_forward_refs()


@dataclass
class CharacterTemplateBase:
    class_info: ClassInfo
    stats: Stats
    race: cython.char
    level_up_gain: LevelUpGain
    spawn: Point3D

    collision_radius: cython.double
    collision_height: cython.double
    load: cython.long


@dataclass
class CharacterTemplateDefaults:
    mp_consume_rate: cython.long = 0
    hp_consume_rate: cython.long = 0

    items: typing.List[cython.long] = field(default_factory=list)


@dataclass
class CharacterTemplate(BaseDataclass, CharacterTemplateDefaults, CharacterTemplateBase):
    @classmethod
    def from_static_template(
        cls,
        template: game.static.character_template.StaticCharacterTemplate,
        sex: Int,
    ):

        class_info = ClassInfo(
            id=template.class_id,
            name=template.class_name,
            base_level=template.level_up_gain.level,
        )

        collision_height = template.male_collision_height
        collision_radius = template.male_collision_radius
        if sex:
            collision_radius = template.female_collision_radius
            collision_height = template.female_collision_height

        template.stats.max_hp = cython.long(template.level_up_gain.hp.base.value)
        template.stats.max_mp = cython.long(template.level_up_gain.mp.base.value)
        template.stats.max_cp = cython.long(template.level_up_gain.cp.base.value)

        return cls(
            class_info=class_info,
            stats=template.stats,
            race=template.race_id,
            level_up_gain=template.level_up_gain,
            spawn=template.spawn,
            collision_radius=collision_radius,
            collision_height=collision_height,
            items=template.items,
            load=template.load,
        )


CharacterTemplate.update_forward_refs()
