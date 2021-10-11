from dataclasses import dataclass, field

import common.datatypes
from common.dataclass import BaseDataclass


@dataclass
class Limits(BaseDataclass):
    inventory: common.datatypes.Int32
    warehouse: common.datatypes.Int32
    freight: common.datatypes.Int32
    sell: common.datatypes.Int32
    buy: common.datatypes.Int32
    dwarf_recipe: common.datatypes.Int32
    common_recipe: common.datatypes.Int32
