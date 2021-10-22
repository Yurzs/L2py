import typing
from dataclasses import dataclass, field

from common.dataclass import BaseDataclass


@dataclass
class ZoneManager(BaseDataclass):
    zones: typing.List[None]
