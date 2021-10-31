from dataclasses import dataclass, field

from common.dataclass import BaseDataclass


@dataclass
class Point3D(BaseDataclass):
    x: Int32 = field(default=0)
    y: Int32 = field(default=0)
    z: Int32 = field(default=0)
