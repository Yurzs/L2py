from pydantic import Extra, Field

from common.ctype import ctype
from common.model import BaseModel
from game.models.structures.object.poly import ObjectPolymorph
from game.models.structures.object.position import Position


class L2Object(BaseModel):
    id: ctype.int32
    name: str
    position: Position
    is_visible: ctype.bool
    poly: ObjectPolymorph = Field(default_factory=ObjectPolymorph)

    class Config(BaseModel.Config):
        extra = Extra.ignore
