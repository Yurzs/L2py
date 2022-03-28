from dataclasses import dataclass, field

from common.dataclass import BaseDataclass
from common.helpers.cython import cython


@dataclass
class Point3D(BaseDataclass):
    x: cython.long = field(default=0)
    y: cython.long = field(default=0)
    z: cython.long = field(default=0)
