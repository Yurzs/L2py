import dataclasses

from common.ctype import ctype
from common.dataclass import BaseDataclass


@dataclasses.dataclass(kw_only=True)
class UpdateChecks(BaseDataclass):
    increase: ctype.int64 = 0
    decrease: ctype.int64 = 0
    interval: ctype.int64 = 0
