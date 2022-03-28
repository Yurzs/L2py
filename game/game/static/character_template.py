import typing
from dataclasses import dataclass

from common.helpers.bytearray import ByteArray
from common.helpers.cython import cython
from game.models.structures.character.stats import Stats
from game.models.structures.character.template import LevelUpGain
from game.models.structures.object.point3d import Point3D
from game.static.static import StaticData


@dataclass
class StaticCharacterTemplate(StaticData):
    spawn: Point3D
    items: typing.List[cython.long]
    class_id: cython.long
    class_name: str
    race_id: cython.long
    stats: Stats
    load: cython.long
    can_craft: cython.char
    male_unk1: cython.float
    male_unk2: cython.float
    male_collision_radius: cython.float
    male_collision_height: cython.float
    female_unk1: cython.float
    female_unk2: cython.float
    female_collision_radius: cython.float
    female_collision_height: cython.float
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
        result.append(cython.long(0x46))
        result.append(self.stats.base.str)
        result.append(cython.long(0x0A))
        result.append(cython.long(0x46))
        result.append(self.stats.base.dex)
        result.append(cython.long(0x0A))
        result.append(cython.long(0x46))
        result.append(self.stats.base.con)
        result.append(cython.long(0x0A))
        result.append(cython.long(0x46))
        result.append(self.stats.base.int)
        result.append(cython.long(0x0A))
        result.append(cython.long(0x46))
        result.append(self.stats.base.wit)
        result.append(cython.long(0x0A))
        result.append(cython.long(0x46))
        result.append(self.stats.base.men)
        result.append(cython.long(0x0A))
        result.append(cython.long(0x46))
        result.append(cython.long(0x0A))
        return result
