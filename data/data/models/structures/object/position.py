from dataclasses import dataclass, field

import data.models.structures.object.point3d
import data.models.structures.world_region
from common.dataclass import BaseDataclass


@dataclass
class Position(BaseDataclass):
    heading_angle: Int32 = field(default=0)
    point3d: data.models.structures.object.point3d.Point3D = (
        data.models.structures.object.point3d.Point3D()
    )
    region: data.models.structures.world_region.WorldRegion = None
    object: "data.models.structures.object.object.L2Object" = field(default=None)
