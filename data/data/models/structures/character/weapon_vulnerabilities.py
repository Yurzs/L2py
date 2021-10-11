from dataclasses import dataclass, field

import common.datatypes
from common.dataclass import BaseDataclass


@dataclass
class WeaponVulnerabilities(BaseDataclass):
    shield: common.datatypes.Int32
    sword: common.datatypes.Int32
    blunt: common.datatypes.Int32
    dagger: common.datatypes.Int32
    bow: common.datatypes.Int32
    pole: common.datatypes.Int32
    etc: common.datatypes.Int32
    fist: common.datatypes.Int32
    dual: common.datatypes.Int32
    dual_fist: common.datatypes.Int32
