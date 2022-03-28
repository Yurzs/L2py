from dataclasses import dataclass, field

from common.dataclass import BaseDataclass


@dataclass
class Limits(BaseDataclass):
    inventory: cython.long
    warehouse: cython.long
    freight: cython.long
    sell: cython.long
    buy: cython.long
    dwarf_recipe: cython.long
    common_recipe: cython.long
