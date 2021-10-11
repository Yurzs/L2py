from dataclasses import dataclass, field

import common.datatypes
from common.dataclass import BaseDataclass


@dataclass
class Skill(BaseDataclass):
    op_type: None
    target_type: None
    type: None
