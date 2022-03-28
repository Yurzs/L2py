from dataclasses import dataclass, field

from common.dataclass import BaseDataclass


@dataclass
class Reflections(BaseDataclass):
    damage_percent: cython.long
    magic_skill: cython.long
    physical_skill: cython.long
    absorb_percent: cython.long
    transfer_percent: cython.long
