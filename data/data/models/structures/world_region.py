from __future__ import annotations

import typing
from dataclasses import dataclass, field

import common.datatypes
from common.dataclass import BaseDataclass

# import data.models.structures.object.object


@dataclass
class WorldRegion(BaseDataclass):
    playable_objects: typing.List["L2Object"]
    visible_objects: typing.List["data.models.structures.object.object.L2Object"]
    neighbours: typing.List["WorldRegion"]
    tile_x: common.datatypes.Int32
    tile_y: common.datatypes.Int32
    active: common.datatypes.Bool
    zone_manager: None


WorldRegion.update_forward_refs(
    # **{"data.models.structures.object.object.L2Object": data.models.structures.object.object.L2Object}
)
