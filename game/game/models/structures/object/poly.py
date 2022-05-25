import dataclasses

from common.ctype import ctype
from common.dataclass import BaseDataclass


@dataclasses.dataclass(kw_only=True)
class ObjectPolymorph(BaseDataclass):
    id: ctype.int32 = 0
    type: ctype.int32 = 0
