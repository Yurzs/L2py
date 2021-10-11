import typing
from dataclasses import dataclass, field

import common.datatypes
from common.helpers.bytearray import ByteArray
from data.models.structures.static.static import StaticData


@dataclass
class CharacterTemplate(StaticData):
    x: common.datatypes.Int32
    y: common.datatypes.Int32
    z: common.datatypes.Int32
    items: typing.List[common.datatypes.Int32]
    class_id: common.datatypes.Int32
    class_name: common.datatypes.UTFString
    race_id: common.datatypes.Int32
    str: common.datatypes.Int32
    con: common.datatypes.Int32
    dex: common.datatypes.Int32
    int: common.datatypes.Int32
    wit: common.datatypes.Int32
    men: common.datatypes.Int32
    physical_attack: common.datatypes.Int32
    physical_defense: common.datatypes.Int32
    magic_attack: common.datatypes.Int32
    magic_defense: common.datatypes.Int32
    physical_attack_speed: common.datatypes.Int32
    magic_attack_speed: common.datatypes.Int32
    accuracy: common.datatypes.Int32
    critical: common.datatypes.Int32
    evasion: common.datatypes.Int32
    move_speed: common.datatypes.Int32
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

    __filepath__ = "static/char_templates.json"

    @classmethod
    def by_id(cls, class_id) -> "CharacterBaseTemplate":
        for template in cls.read_file():
            if template.class_id == class_id:
                return template

    def encode(self):
        result = ByteArray(b"")
        result.append(self.race_id)
        result.append(self.class_id)
        result.append(common.datatypes.Int32(0x46))
        result.append(self.str)
        result.append(common.datatypes.Int32(0x0A))
        result.append(common.datatypes.Int32(0x46))
        result.append(self.dex)
        result.append(common.datatypes.Int32(0x0A))
        result.append(common.datatypes.Int32(0x46))
        result.append(self.con)
        result.append(common.datatypes.Int32(0x0A))
        result.append(common.datatypes.Int32(0x46))
        result.append(self.int)
        result.append(common.datatypes.Int32(0x0A))
        result.append(common.datatypes.Int32(0x46))
        result.append(self.wit)
        result.append(common.datatypes.Int32(0x0A))
        result.append(common.datatypes.Int32(0x46))
        result.append(self.men)
        result.append(common.datatypes.Int32(0x0A))
        result.append(common.datatypes.Int32(0x46))
        result.append(common.datatypes.Int32(0x0A))
        return result
