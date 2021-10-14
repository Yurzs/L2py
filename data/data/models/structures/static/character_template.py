import typing
from dataclasses import dataclass, field

import common.datatypes
from common.helpers.bytearray import ByteArray
from data.models.structures.character.stats import BaseStats, Stats
from data.models.structures.character.template import CharacterTemplate, LevelUpGain
from data.models.structures.object.point3d import Point3D
from data.models.structures.static.static import StaticData


@dataclass
class StaticCharacterTemplate(StaticData):
    spawn: Point3D
    items: typing.List[common.datatypes.Int32]
    class_id: common.datatypes.Int32
    class_name: common.datatypes.UTFString
    race_id: common.datatypes.Int32
    stats: Stats
    load: common.datatypes.Int32
    can_craft: common.datatypes.Int8
    male_unk1: common.datatypes.Float
    male_unk2: common.datatypes.Float
    male_collision_radius: common.datatypes.Float
    male_collision_height: common.datatypes.Float
    female_unk1: common.datatypes.Float
    female_unk2: common.datatypes.Float
    female_collision_radius: common.datatypes.Float
    female_collision_height: common.datatypes.Float
    level_up_gain: LevelUpGain

    __filepath__ = "static/char_templates.json"

    @classmethod
    def by_id(cls, class_id) -> "CharacterBaseTemplate":
        for template in cls.read_file():
            if template.class_id == class_id:
                return template

    def encode(self):
        result = ByteArray(self.race_id)
        result.append(self.class_id)
        result.append(common.datatypes.Int32(0x46))
        result.append(self.stats.base.str)
        result.append(common.datatypes.Int32(0x0A))
        result.append(common.datatypes.Int32(0x46))
        result.append(self.stats.base.dex)
        result.append(common.datatypes.Int32(0x0A))
        result.append(common.datatypes.Int32(0x46))
        result.append(self.stats.base.con)
        result.append(common.datatypes.Int32(0x0A))
        result.append(common.datatypes.Int32(0x46))
        result.append(self.stats.base.int)
        result.append(common.datatypes.Int32(0x0A))
        result.append(common.datatypes.Int32(0x46))
        result.append(self.stats.base.wit)
        result.append(common.datatypes.Int32(0x0A))
        result.append(common.datatypes.Int32(0x46))
        result.append(self.stats.base.men)
        result.append(common.datatypes.Int32(0x0A))
        result.append(common.datatypes.Int32(0x46))
        result.append(common.datatypes.Int32(0x0A))
        return result
