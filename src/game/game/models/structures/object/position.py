import dataclasses

from src.common.common.ctype import ctype
from src.common.common.dataclass import BaseDataclass
from src.game.game.models.structures.object.point3d import Point3D
from src.game.game.models.structures.world_region import WorldRegion


@dataclasses.dataclass(kw_only=True)
class Position(BaseDataclass):
    heading_angle: ctype.int32
    point3d: Point3D
    region: WorldRegion = dataclasses.field(default_factory=WorldRegion)
