from dataclasses import dataclass, field

import common.datatypes
from common.dataclass import BaseDataclass


@dataclass
class Resists(BaseDataclass):
    breath: common.datatypes.Int32 = field(default=0)
    aggression: common.datatypes.Int32 = field(default=0)
    confusion: common.datatypes.Int32 = field(default=0)
    movement: common.datatypes.Int32 = field(default=0)
    sleep: common.datatypes.Int32 = field(default=0)
    fire: common.datatypes.Int32 = field(default=0)
    wind: common.datatypes.Int32 = field(default=0)
    water: common.datatypes.Int32 = field(default=0)
    earth: common.datatypes.Int32 = field(default=0)
    holy: common.datatypes.Int32 = field(default=0)
    dark: common.datatypes.Int32 = field(default=0)
