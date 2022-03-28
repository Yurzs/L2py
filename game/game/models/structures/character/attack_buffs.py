from dataclasses import dataclass, field

from common.dataclass import BaseDataclass


@dataclass
class AttacksBuffs(BaseDataclass):
    physical_plants: cython.long
    physical_insects: cython.long
    physical_animals: cython.long
    physical_monsters: cython.long
    physical_dragons: cython.long
    physical_undead: cython.long
