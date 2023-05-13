from pydantic import validator

from common.ctype import ctype
from common.model import BaseModel


class CharacterAppearance(BaseModel):
    face_id: ctype.int32
    hair_style: ctype.int32
    hair_color: ctype.int32
    sex: ctype.bool  # 0 = male, 1 = female

    @classmethod
    @validator("sex")
    def validate_male_or_female(cls, v):
        if int(v) not in [0, 1]:
            raise ValueError("Sex value only can be 0 or 1")
        return v
