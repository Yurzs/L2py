from pydantic import Field

from common.ctype import ctype
from common.model import BaseModel
from game.models.structures.object.point3d import Point3D
from game.models.structures.world_region import WorldRegion


class Position(BaseModel):
    heading_angle: ctype.int32
    point3d: Point3D
    region: WorldRegion = Field(default_factory=WorldRegion)
