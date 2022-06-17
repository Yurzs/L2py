import dataclasses

from src.common.common.ctype import ctype
from src.common.common.dataclass import BaseDataclass


@dataclasses.dataclass(kw_only=True)
class CharacterAppearance(BaseDataclass):
    face_id: ctype.int32
    hair_style: ctype.int32
    hair_color: ctype.int32
    sex: ctype.bool  # 0 = male, 1 = female
