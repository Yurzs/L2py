import typing
from dataclasses import dataclass, field

import common.datatypes
from common.dataclass import BaseDataclass
from data.models.structures.zone.farm import ZoneFarm


@dataclass
class ZoneType(BaseDataclass):
    zone: ZoneFarm
    characters: typing.List[None]  # TODO
    min_lvl: common.datatypes.Int32
    max_lvl: common.datatypes.Int32
    races: typing.List[common.datatypes.Int32]
    classes: typing.List[common.datatypes.Int32]
