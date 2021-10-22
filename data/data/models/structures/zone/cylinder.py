from dataclasses import dataclass, field

from data.models.structures.zone.farm import ZoneFarm


@dataclass
class ZoneCylinder(ZoneFarm):
    x: Int32
    y: Int32
    z1: Int32
    z2: Int32
    radiant: Int32
    radiantS: Int32
