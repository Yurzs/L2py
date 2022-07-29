import typing
from dataclasses import dataclass

from common.ctype import ctype
from common.misc import extend_bytearray
from game.models.structures.character.stats import Stats
from game.models.structures.character.template import LevelUpGain
from game.models.structures.object.point3d import Point3D
from game.static.static import StaticData


@dataclass(kw_only=True)
class StaticCharacterTemplate(StaticData):
    spawn: Point3D
    items: list[ctype.int32]
    class_id: ctype.int32
    class_name: str
    race_id: ctype.int32
    stats: Stats
    load: ctype.int32
    can_craft: ctype.int8
    male_unk1: ctype.float
    male_unk2: ctype.float
    male_collision_radius: ctype.double
    male_collision_height: ctype.double
    female_unk1: ctype.float
    female_unk2: ctype.float
    female_collision_radius: ctype.double
    female_collision_height: ctype.double
    level_up_gain: LevelUpGain
    base_level: ctype.int32

    __filepath__ = "game/data/char_templates.json"

    __encode__ = ["race_id", "class_id", ""]

    @classmethod
    def by_id(cls, class_id) -> "CharacterBaseTemplate":
        for template in cls.read_file():
            if template.class_id == class_id:
                return template

    def encode(self, strings_format="utf-16-le") -> bytearray:
        result = bytearray()

        extend_bytearray(
            result,
            [
                self.race_id,
                self.class_id,
                ctype.int32(0x46),
                self.stats.base.STR,
                ctype.int32(0x0A),
                ctype.int32(0x46),
                self.stats.base.DEX,
                ctype.int32(0x0A),
                ctype.int32(0x46),
                self.stats.base.CON,
                ctype.int32(0x0A),
                ctype.int32(0x46),
                self.stats.base.INT,
                ctype.int32(0x0A),
                ctype.int32(0x46),
                self.stats.base.WIT,
                ctype.int32(0x0A),
                ctype.int32(0x46),
                self.stats.base.MEN,
                ctype.int32(0x0A),
                # ctype.int32(0x46),
                # ctype.int32(0x0A),
            ],
        )

        return result

    # @StaticData.encode_fields
    # def encode(self):
    #     return [
    #         (self.race_id, ctype.int32),
    #         (self.class_id, ctype.int32),
    #         (0x46, ctype.int32),
    #         (self.stats.base.str, ctype.int32),
    #         (0x0A, ctype.int32),
    #         (0x46, ctype.int32),
    #         (self.stats.base.dex, ctype.int32),
    #         (0x0A, ctype.int32),
    #         (0x46, ctype.int32),
    #         (self.stats.base.con, ctype.int32),
    #         (0x0A, ctype.int32),
    #         (0x46, ctype.int32),
    #         (self.stats.base.int, ctype.int32),
    #         (0x0A, ctype.int32),
    #         (0x46, ctype.int32),
    #         (self.stats.base.wit, ctype.int32),
    #         (0x0A, ctype.int32),
    #         (0x46, ctype.int32),
    #         (self.stats.base.men, ctype.int32),
    #         (0x0A, ctype.int32),
    #         (0x46, ctype.int32),
    #         (0x0A, ctype.int32),
    #     ]
