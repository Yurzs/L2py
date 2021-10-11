from dataclasses import dataclass, field

import common.datatypes
from data.models.structures.zone.farm import ZoneFarm


@dataclass
class ZoneCylinder(ZoneFarm):
    x: common.datatypes.Int32
    y: common.datatypes.Int32
    z1: common.datatypes.Int32
    z2: common.datatypes.Int32
    radiant: common.datatypes.Int32
    radiantS: common.datatypes.Int32
