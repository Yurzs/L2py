from dataclasses import dataclass, field

import common.datatypes
from common.dataclass import BaseDataclass


@dataclass
class ConsumeRates(BaseDataclass):
    mp: common.datatypes.Int32
    hp: common.datatypes.Int32
