import dataclasses

from src.common.common.ctype import ctype
from src.common.common.dataclass import BaseDataclass


@dataclasses.dataclass(kw_only=True)
class ObjectPolymorph(BaseDataclass):
    id: ctype.int32 = 0
    type: ctype.int32 = 0
