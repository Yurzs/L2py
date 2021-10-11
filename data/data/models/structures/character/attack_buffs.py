from dataclasses import dataclass, field

import common.datatypes
from common.dataclass import BaseDataclass


@dataclass
class AttacksBuffs(BaseDataclass):
    physical_plants: common.datatypes.Int32
    physical_insects: common.datatypes.Int32
    physical_animals: common.datatypes.Int32
    physical_monsters: common.datatypes.Int32
    physical_dragons: common.datatypes.Int32
    physical_undead: common.datatypes.Int32
