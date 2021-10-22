from dataclasses import dataclass, field

from common.dataclass import BaseDataclass


@dataclass
class AttacksBuffs(BaseDataclass):
    physical_plants: Int32
    physical_insects: Int32
    physical_animals: Int32
    physical_monsters: Int32
    physical_dragons: Int32
    physical_undead: Int32
