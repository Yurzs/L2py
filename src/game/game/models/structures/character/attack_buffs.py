import dataclasses

from src.common.common.ctype import ctype
from src.common.common.dataclass import BaseDataclass


@dataclasses.dataclass(kw_only=True)
class AttacksBuffs(BaseDataclass):
    physical_plants: ctype.int32
    physical_insects: ctype.int32
    physical_animals: ctype.int32
    physical_monsters: ctype.int32
    physical_dragons: ctype.int32
    physical_undead: ctype.int32
