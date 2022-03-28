import typing
from dataclasses import dataclass, field

from common.dataclass import BaseDataclass
from game.models.structures.zone.farm import ZoneFarm


@dataclass
class ZoneType(BaseDataclass):
    zone: ZoneFarm
    characters: typing.List[None]  # TODO
    min_lvl: cython.long
    max_lvl: cython.long
    races: typing.List[cython.long]
    classes: typing.List[cython.long]
