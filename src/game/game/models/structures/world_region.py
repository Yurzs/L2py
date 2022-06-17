import dataclasses
from dataclasses import field

from src.common.common.ctype import ctype
from src.common.common.dataclass import BaseDataclass


@dataclasses.dataclass(kw_only=True)
class WorldRegion(BaseDataclass):
    tile_x: ctype.int32 = 0
    tile_y: ctype.int32 = 0
    active: ctype.int32 = 0

    playable_objects: list[ctype.int32] = field(default_factory=list)
    visible_objects: list[ctype.int32] = field(default_factory=list)
    neighbours: list["WorldRegion"] = field(default_factory=list)
