from dataclasses import dataclass, field

from common.dataclass import BaseDataclass


@dataclass
class ConsumeRates(BaseDataclass):
    mp: Int32
    hp: Int32
