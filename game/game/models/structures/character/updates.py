from dataclasses import dataclass, field

from common.dataclass import BaseDataclass
from common.helpers.cython import cython


@dataclass
class UpdateChecks(BaseDataclass):
    increase: cython.longlong = field(default=0)
    decrease: cython.longlong = field(default=0)
    interval: cython.longlong = field(default=0)
