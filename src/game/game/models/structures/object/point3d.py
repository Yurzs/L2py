import dataclasses

from src.common.common.ctype import ctype
from src.common.common.dataclass import BaseDataclass


@dataclasses.dataclass(kw_only=True)
class Point3D(BaseDataclass):
    x: ctype.int32
    y: ctype.int32
    z: ctype.int32

    __encode__ = ["x", "y", "z"]
