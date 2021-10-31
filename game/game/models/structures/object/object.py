from dataclasses import dataclass, field

from common.dataclass import BaseDataclass
from game.models.structures.object.poly import ObjectPolymorph
from game.models.structures.object.position import Position


@dataclass
class L2ObjectBases:
    id: Int32
    name: UTFString
    position: Position


@dataclass
class L2ObjectDefaults:
    is_visible: Bool = field(default=True)
    poly: ObjectPolymorph = field(default=ObjectPolymorph())


@dataclass
class L2Object(BaseDataclass, L2ObjectDefaults, L2ObjectBases):
    pass
