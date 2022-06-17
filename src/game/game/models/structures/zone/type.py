import typing
from dataclasses import dataclass, field

from src.common.common.ctype import ctype
from src.common.common.dataclass import BaseDataclass
from src.game.game.models.structures.zone.farm import ZoneFarm


@dataclass(kw_only=True)
class ZoneType(BaseDataclass):
    zone: ZoneFarm
    characters: typing.List[None]  # TODO
    min_lvl: ctype.int32
    max_lvl: ctype.int32
    races: typing.List[ctype.int32]
    classes: typing.List[ctype.int32]
