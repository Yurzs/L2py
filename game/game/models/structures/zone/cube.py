from dataclasses import dataclass, field

from game.models.structures.zone.farm import ZoneFarm


@dataclass
class ZoneCube(ZoneFarm):
    x1: Int32
    x2: Int32
    y1: Int32
    y2: Int32
    z1: Int32
    z2: Int32
