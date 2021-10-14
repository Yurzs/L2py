from __future__ import annotations

import typing
from dataclasses import dataclass, field

import common.datatypes
import data.models.structures.static.character_template
from common.dataclass import BaseDataclass
from data.models.structures.character.stats import Stats

# from data.models.structures.item.item import Item
from data.models.structures.object.point3d import Point3D


@dataclass
class LevelUpIncrease:
    base: common.datatypes.Float = 1
    add: common.datatypes.Float = 1
    mod: common.datatypes.Float = 1


# LevelUpIncrease.update_forward_refs()


@dataclass
class LevelUpGain:
    level: common.datatypes.Int32 = 1
    hp: LevelUpIncrease = LevelUpIncrease()
    cp: LevelUpIncrease = LevelUpIncrease()
    mp: LevelUpIncrease = LevelUpIncrease()


# LevelUpGain.update_forward_refs()


@dataclass
class ClassInfo:
    id: common.datatypes.Int8 = 1
    name: common.datatypes.UTFString = "Human Fighter"
    base_level: common.datatypes.Int32 = 1


@dataclass
class CharacterTemplateBase:
    class_info: ClassInfo
    stats: Stats
    race: common.datatypes.Int8
    level_up_gain: LevelUpGain
    spawn: Point3D

    collision_radius: common.datatypes.Float
    collision_height: common.datatypes.Float


@dataclass
class CharacterTemplateDefaults:
    mp_consume_rate: common.datatypes.Int32 = 0
    hp_consume_rate: common.datatypes.Int32 = 0

    items: typing.List[common.datatypes.Int32] = field(default_factory=list)


@dataclass
class CharacterTemplate(BaseDataclass, CharacterTemplateDefaults, CharacterTemplateBase):
    @classmethod
    def from_static_template(
        cls,
        template: data.models.structures.static.character_template.StaticCharacterTemplate,
        sex: common.datatypes.Int,
    ):

        class_info = ClassInfo(
            id=template.class_id, name=template.class_name, base_level=template.level_up_gain.level
        )

        collision_height = template.male_collision_height
        collision_radius = template.male_collision_radius
        if sex:
            collision_radius = template.female_collision_radius
            collision_height = template.female_collision_height

        template.stats.max_hp = template.level_up_gain.hp.base
        template.stats.max_mp = template.level_up_gain.mp.base
        template.stats.max_cp = template.level_up_gain.cp.base

        return cls(
            class_info=class_info,
            stats=template.stats,
            race=template.race_id,
            level_up_gain=template.level_up_gain,
            spawn=template.spawn,
            collision_radius=collision_radius,
            collision_height=collision_height,
            items=template.items,
        )


CharacterTemplate.update_forward_refs()
