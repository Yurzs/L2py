from dataclasses import dataclass, field

from common.dataclass import BaseDataclass


@dataclass
class WeaponVulnerabilities(BaseDataclass):
    shield: Int32
    sword: Int32
    blunt: Int32
    dagger: Int32
    bow: Int32
    pole: Int32
    etc: Int32
    fist: Int32
    dual: Int32
    dual_fist: Int32
