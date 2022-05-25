import dataclasses

from common.ctype import ctype
from common.dataclass import BaseDataclass


@dataclasses.dataclass(kw_only=True)
class Reflections(BaseDataclass):
    damage_percent: ctype.int32
    magic_skill: ctype.int32
    physical_skill: ctype.int32
    absorb_percent: ctype.int32
    transfer_percent: ctype.int32
