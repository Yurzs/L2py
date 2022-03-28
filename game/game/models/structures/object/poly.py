from __future__ import annotations

from dataclasses import dataclass, field

import game.models.structures.object.object
from common.dataclass import BaseDataclass


@dataclass
class ObjectPolymorph(BaseDataclass):
    id: cython.long = None
    type: cython.long = None
    object: game.models.structures.object.object.L2Object = field(default=None)
