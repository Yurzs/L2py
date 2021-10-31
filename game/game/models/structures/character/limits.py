from dataclasses import dataclass, field

from common.dataclass import BaseDataclass


@dataclass
class Limits(BaseDataclass):
    inventory: Int32
    warehouse: Int32
    freight: Int32
    sell: Int32
    buy: Int32
    dwarf_recipe: Int32
    common_recipe: Int32
