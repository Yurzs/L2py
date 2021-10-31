from dataclasses import dataclass, field

import game.models.structures.object.point3d
import game.models.structures.world_region
from common.dataclass import BaseDataclass


@dataclass
class Position(BaseDataclass):
    heading_angle: Int32 = field(default=0)
    point3d: game.models.structures.object.point3d.Point3D = (
        game.models.structures.object.point3d.Point3D()
    )
    region: game.models.structures.world_region.WorldRegion = None
    object: "game.models.structures.object.object.L2Object" = field(default=None)
