import dataclasses

from src.common.common.ctype import ctype
from src.common.common.dataclass import BaseDataclass


@dataclasses.dataclass(kw_only=True)
class WeaponVulnerabilities(BaseDataclass):
    shield: ctype.int32 = 0
    sword: ctype.int32 = 0
    blunt: ctype.int32 = 0
    dagger: ctype.int32 = 0
    bow: ctype.int32 = 0
    pole: ctype.int32 = 0
    etc: ctype.int32 = 0
    fist: ctype.int32 = 0
    dual: ctype.int32 = 0
    dual_fist: ctype.int32 = 0
