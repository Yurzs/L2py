import dataclasses
from dataclasses import field

from src.common.common.ctype import ctype
from src.common.common.dataclass import BaseDataclass


@dataclasses.dataclass(kw_only=True)
class Resists(BaseDataclass):
    breath: ctype.int32 = field(default=0)
    aggression: ctype.int32 = field(default=0)
    confusion: ctype.int32 = field(default=0)
    movement: ctype.int32 = field(default=0)
    sleep: ctype.int32 = field(default=0)
    fire: ctype.int32 = field(default=0)
    wind: ctype.int32 = field(default=0)
    water: ctype.int32 = field(default=0)
    earth: ctype.int32 = field(default=0)
    holy: ctype.int32 = field(default=0)
    dark: ctype.int32 = field(default=0)
