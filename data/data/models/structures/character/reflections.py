from dataclasses import dataclass, field

import common.datatypes
from common.dataclass import BaseDataclass


@dataclass
class Reflections(BaseDataclass):
    damage_percent: common.datatypes.Int32
    magic_skill: common.datatypes.Int32
    physical_skill: common.datatypes.Int32
    absorb_percent: common.datatypes.Int32
    transfer_percent: common.datatypes.Int32
