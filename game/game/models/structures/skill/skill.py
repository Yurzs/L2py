from common.ctype import ctype
from common.model import BaseModel


class Skill(BaseModel):
    id: ctype.int32 = 0
    activation_type: str = ""
    target_type: ctype.int32 = 0
    type: ctype.int32 = 0
