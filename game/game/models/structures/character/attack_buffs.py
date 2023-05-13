from common.ctype import ctype
from common.model import BaseModel


class AttacksBuffs(BaseModel):
    physical_plants: ctype.int32
    physical_insects: ctype.int32
    physical_animals: ctype.int32
    physical_monsters: ctype.int32
    physical_dragons: ctype.int32
    physical_undead: ctype.int32
