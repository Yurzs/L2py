from dataclasses import dataclass, field

from common.dataclass import BaseDataclass


@dataclass
class Reflections(BaseDataclass):
    damage_percent: Int32
    magic_skill: Int32
    physical_skill: Int32
    absorb_percent: Int32
    transfer_percent: Int32
