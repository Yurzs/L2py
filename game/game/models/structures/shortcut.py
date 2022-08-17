import dataclasses

from common.ctype import ctype
from common.dataclass import BaseDataclass


@dataclasses.dataclass(kw_only=True)
class Shortcut(BaseDataclass):
    slot: ctype.int32
    page: ctype.int32
    type: ctype.int32
    id: ctype.int32
    level: ctype.int32
