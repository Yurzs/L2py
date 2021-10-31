from dataclasses import dataclass, field

from common.dataclass import BaseDataclass


@dataclass
class UpdateChecks(BaseDataclass):
    increase: Int64 = field(default=0)
    decrease: Int64 = field(default=0)
    interval: Int64 = field(default=0)
