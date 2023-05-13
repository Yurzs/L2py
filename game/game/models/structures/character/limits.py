from common.ctype import ctype
from common.model import BaseModel


class Limits(BaseModel):
    inventory: ctype.int32
    warehouse: ctype.int32
    freight: ctype.int32
    sell: ctype.int32
    buy: ctype.int32
    dwarf_recipe: ctype.int32
    common_recipe: ctype.int32
