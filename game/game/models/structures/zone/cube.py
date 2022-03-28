from dataclasses import dataclass, field

from game.models.structures.zone.farm import ZoneFarm


@dataclass
class ZoneCube(ZoneFarm):
    x1: cython.long
    x2: cython.long
    y1: cython.long
    y2: cython.long
    z1: cython.long
    z2: cython.long
