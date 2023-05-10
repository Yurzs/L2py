import typing

from common.ctype import ctype
from common.model import BaseModel
from game.models.structures.zone.farm import ZoneFarm


class ZoneType(BaseModel):
    zone: ZoneFarm
    characters: list[None]  # TODO
    min_lvl: ctype.int32
    max_lvl: ctype.int32
    races: list[ctype.int32]
    classes: list[ctype.int32]
