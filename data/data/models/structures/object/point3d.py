from dataclasses import dataclass, field

import common.datatypes
from common.dataclass import BaseDataclass


@dataclass
class Point3D(BaseDataclass):
    x: common.datatypes.Int32 = field(default=0)
    y: common.datatypes.Int32 = field(default=0)
    z: common.datatypes.Int32 = field(default=0)
