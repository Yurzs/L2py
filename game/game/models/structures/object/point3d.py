from common.ctype import ctype
from common.model import BaseModel


class Point3D(BaseModel):
    x: ctype.int32
    y: ctype.int32
    z: ctype.int32
