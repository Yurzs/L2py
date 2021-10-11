from dataclasses import dataclass, field

import common.datatypes
from common.dataclass import BaseDataclass


@dataclass
class UpdateChecks(BaseDataclass):
    increase: common.datatypes.Int64 = field(default=0)
    decrease: common.datatypes.Int64 = field(default=0)
    interval: common.datatypes.Int64 = field(default=0)
