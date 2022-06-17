from dataclasses import dataclass, field

from src.common.common.ctype import ctype
from src.game.game.models.structures.zone.farm import ZoneFarm


@dataclass(kw_only=True)
class ZoneCylinder(ZoneFarm):
    x: ctype.int32
    y: ctype.int32
    z1: ctype.int32
    z2: ctype.int32
    radiant: ctype.int32
    radiantS: ctype.int32
