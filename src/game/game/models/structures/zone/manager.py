import typing
from dataclasses import dataclass, field

from src.common.common.dataclass import BaseDataclass


@dataclass(kw_only=True)
class ZoneManager(BaseDataclass):
    zones: typing.List[None]
