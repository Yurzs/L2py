import dataclasses

from src.common.common.ctype import ctype
from src.common.common.dataclass import BaseDataclass
from src.game.game.models.structures.object.poly import ObjectPolymorph
from src.game.game.models.structures.object.position import Position


@dataclasses.dataclass(kw_only=True)
class L2Object(BaseDataclass):
    id: ctype.int32
    name: str
    position: Position
    is_visible: ctype.bool
    poly: ObjectPolymorph = dataclasses.field(default_factory=ObjectPolymorph)
