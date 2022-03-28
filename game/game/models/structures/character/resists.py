from dataclasses import dataclass, field

from common.dataclass import BaseDataclass
from common.helpers.cython import cython


@dataclass
class Resists(BaseDataclass):
    breath: cython.long = field(default=0)
    aggression: cython.long = field(default=0)
    confusion: cython.long = field(default=0)
    movement: cython.long = field(default=0)
    sleep: cython.long = field(default=0)
    fire: cython.long = field(default=0)
    wind: cython.long = field(default=0)
    water: cython.long = field(default=0)
    earth: cython.long = field(default=0)
    holy: cython.long = field(default=0)
    dark: cython.long = field(default=0)
