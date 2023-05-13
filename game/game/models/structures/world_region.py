from pydantic import Field

from common.ctype import ctype
from common.model import BaseModel


class WorldRegion(BaseModel):
    tile_x: ctype.int32 = 0
    tile_y: ctype.int32 = 0
    active: ctype.int32 = 0

    playable_objects: list[ctype.int32] = Field(default_factory=list, exclude=True)
    visible_objects: list[ctype.int32] = Field(default_factory=list, exclude=True)
    neighbours: list["WorldRegion"] = Field(default_factory=list, exclude=True)
