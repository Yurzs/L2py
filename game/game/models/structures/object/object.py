import dataclasses

from common.ctype import ctype
from common.dataclass import BaseDataclass
from game.models.structures.object.poly import ObjectPolymorph
from game.models.structures.object.position import Position


@dataclasses.dataclass(kw_only=True)
class L2Object(BaseDataclass):
    id: ctype.int32
    name: str
    position: Position
    is_visible: ctype.bool
    poly: ObjectPolymorph = dataclasses.field(default_factory=ObjectPolymorph)
