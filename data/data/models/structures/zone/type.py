import typing
from dataclasses import dataclass, field

from common.dataclass import BaseDataclass
from data.models.structures.zone.farm import ZoneFarm


@dataclass
class ZoneType(BaseDataclass):
    zone: ZoneFarm
    characters: typing.List[None]  # TODO
    min_lvl: Int32
    max_lvl: Int32
    races: typing.List[Int32]
    classes: typing.List[Int32]
