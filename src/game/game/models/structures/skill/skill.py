import dataclasses

from src.common.common.ctype import ctype
from src.common.common.dataclass import BaseDataclass


@dataclasses.dataclass(kw_only=True)
class Skill(BaseDataclass):
    id: ctype.int32 = 0
    activation_type: str = ""
    target_type: ctype.int32 = 0
    type: ctype.int32 = 0

    __encode__ = ["id"]
