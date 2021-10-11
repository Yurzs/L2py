import typing
from dataclasses import dataclass, field

import common.datatypes
from common.dataclass import BaseDataclass


@dataclass
class ZoneManager(BaseDataclass):
    zones: typing.List[None]
