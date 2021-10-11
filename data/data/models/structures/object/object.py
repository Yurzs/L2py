from dataclasses import dataclass, field

import common.datatypes
from common.dataclass import BaseDataclass
from data.models.structures.object.poly import ObjectPolymorph
from data.models.structures.object.position import Position


@dataclass
class L2Object(BaseDataclass):
    id: common.datatypes.Int32
    is_visible: common.datatypes.Bool = field(default=True)
    name: common.datatypes.UTFString = field(default="")
    poly: ObjectPolymorph = field(default=ObjectPolymorph())
    position: Position = field(default=Position())
