from __future__ import annotations

from dataclasses import dataclass, field

import data.models.structures.object.object
from common.dataclass import BaseDataclass


@dataclass
class ObjectPolymorph(BaseDataclass):
    id: Int32 = None
    type: Int32 = None
    object: data.models.structures.object.object.L2Object = field(default=None)
