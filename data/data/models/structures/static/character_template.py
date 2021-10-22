import typing
from dataclasses import dataclass, field

from common.helpers.bytearray import ByteArray
from data.models.structures.character.stats import BaseStats, Stats
from data.models.structures.character.template import CharacterTemplate, LevelUpGain
from data.models.structures.object.point3d import Point3D
from data.models.structures.static.static import StaticData


@dataclass
class StaticCharacterTemplate(StaticData):
    spawn: Point3D
    items: typing.List[Int32]
    class_id: Int32
    class_name: UTFString
    race_id: Int32
    stats: Stats
    load: Int32
    can_craft: Int8
    male_unk1: Float
    male_unk2: Float
    male_collision_radius: Float
    male_collision_height: Float
    female_unk1: Float
    female_unk2: Float
    female_collision_radius: Float
    female_collision_height: Float
    level_up_gain: LevelUpGain

    __filepath__ = "data/char_templates.json"

    @classmethod
    def by_id(cls, class_id) -> "CharacterBaseTemplate":
        for template in cls.read_file():
            if template.class_id == class_id:
                return template

    def encode(self):
        result = ByteArray(self.race_id)
        result.append(self.class_id)
        result.append(Int32(0x46))
        result.append(self.stats.base.str)
        result.append(Int32(0x0A))
        result.append(Int32(0x46))
        result.append(self.stats.base.dex)
        result.append(Int32(0x0A))
        result.append(Int32(0x46))
        result.append(self.stats.base.con)
        result.append(Int32(0x0A))
        result.append(Int32(0x46))
        result.append(self.stats.base.int)
        result.append(Int32(0x0A))
        result.append(Int32(0x46))
        result.append(self.stats.base.wit)
        result.append(Int32(0x0A))
        result.append(Int32(0x46))
        result.append(self.stats.base.men)
        result.append(Int32(0x0A))
        result.append(Int32(0x46))
        result.append(Int32(0x0A))
        return result
