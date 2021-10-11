from __future__ import annotations

from dataclasses import dataclass, field

import common.datatypes
import data.models.structures.object.object
from common.dataclass import BaseDataclass


@dataclass
class ObjectPolymorph(BaseDataclass):
    id: common.datatypes.Int32 = None
    type: common.datatypes.Int32 = None
    object: data.models.structures.object.object.L2Object = field(default=None)
