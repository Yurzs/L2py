from dataclasses import dataclass, field

from game.models.structures.zone.farm import ZoneFarm


@dataclass
class ZoneCylinder(ZoneFarm):
    x: cython.long
    y: cython.long
    z1: cython.long
    z2: cython.long
    radiant: cython.long
    radiantS: cython.long
