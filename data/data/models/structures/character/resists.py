from dataclasses import dataclass, field

from common.dataclass import BaseDataclass


@dataclass
class Resists(BaseDataclass):
    breath: Int32 = field(default=0)
    aggression: Int32 = field(default=0)
    confusion: Int32 = field(default=0)
    movement: Int32 = field(default=0)
    sleep: Int32 = field(default=0)
    fire: Int32 = field(default=0)
    wind: Int32 = field(default=0)
    water: Int32 = field(default=0)
    earth: Int32 = field(default=0)
    holy: Int32 = field(default=0)
    dark: Int32 = field(default=0)
