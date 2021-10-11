from dataclasses import dataclass, field

import common.datatypes
from data.models.structures.zone.farm import ZoneFarm


@dataclass
class ZoneCube(ZoneFarm):
    x1: common.datatypes.Int32
    x2: common.datatypes.Int32
    y1: common.datatypes.Int32
    y2: common.datatypes.Int32
    z1: common.datatypes.Int32
    z2: common.datatypes.Int32
