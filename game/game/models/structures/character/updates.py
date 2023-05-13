from common.ctype import ctype
from common.model import BaseModel


class UpdateChecks(BaseModel):
    increase: ctype.int64 = 0
    decrease: ctype.int64 = 0
    interval: ctype.int64 = 0
