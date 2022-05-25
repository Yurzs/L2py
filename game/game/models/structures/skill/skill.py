import dataclasses

from common.ctype import ctype
from common.dataclass import BaseDataclass


@dataclasses.dataclass(kw_only=True)
class Skill(BaseDataclass):
    id: ctype.int32 = 0
    activation_type: str = ""
    target_type: ctype.int32 = 0
    type: ctype.int32 = 0

    __encode__ = ["id"]
