import dataclasses

from src.common.common.ctype import ctype
from src.common.common.dataclass import BaseDataclass


@dataclasses.dataclass(kw_only=True)
class Limits(BaseDataclass):
    inventory: ctype.int32
    warehouse: ctype.int32
    freight: ctype.int32
    sell: ctype.int32
    buy: ctype.int32
    dwarf_recipe: ctype.int32
    common_recipe: ctype.int32
