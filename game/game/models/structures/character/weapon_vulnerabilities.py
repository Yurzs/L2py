from dataclasses import dataclass, field

from common.dataclass import BaseDataclass


@dataclass
class WeaponVulnerabilities(BaseDataclass):
    shield: cython.long
    sword: cython.long
    blunt: cython.long
    dagger: cython.long
    bow: cython.long
    pole: cython.long
    etc: cython.long
    fist: cython.long
    dual: cython.long
    dual_fist: cython.long
