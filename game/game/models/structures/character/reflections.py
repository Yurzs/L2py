from common.ctype import ctype
from common.model import BaseModel


class Reflections(BaseModel):
    damage_percent: ctype.int32
    magic_skill: ctype.int32
    physical_skill: ctype.int32
    absorb_percent: ctype.int32
    transfer_percent: ctype.int32
