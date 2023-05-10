from common.ctype import ctype
from common.model import BaseModel


class Resists(BaseModel):
    breath: ctype.int32 = 0
    aggression: ctype.int32 = 0
    confusion: ctype.int32 = 0
    movement: ctype.int32 = 0
    sleep: ctype.int32 = 0
    fire: ctype.int32 = 0
    wind: ctype.int32 = 0
    water: ctype.int32 = 0
    earth: ctype.int32 = 0
    holy: ctype.int32 = 0
    dark: ctype.int32 = 0
