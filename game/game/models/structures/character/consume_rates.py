from common.ctype import ctype
from common.model import BaseModel


class ConsumeRates(BaseModel):
    mp: ctype.int32
    hp: ctype.int32
