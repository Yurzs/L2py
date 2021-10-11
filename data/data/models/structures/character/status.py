from dataclasses import dataclass, field

import common.datatypes
from common.dataclass import BaseDataclass


@dataclass
class Status(BaseDataclass):
    cp: common.datatypes.Double = 0
    hp: common.datatypes.Double = 0
    mp: common.datatypes.Double = 0
