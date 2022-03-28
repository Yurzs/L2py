from dataclasses import dataclass, field

from common.dataclass import BaseDataclass


@dataclass
class ConsumeRates(BaseDataclass):
    mp: cython.long
    hp: cython.long
