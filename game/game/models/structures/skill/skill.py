from dataclasses import dataclass, field

from common.dataclass import BaseDataclass


@dataclass
class Skill(BaseDataclass):
    activation_type: String
    target_type: None
    type: None
