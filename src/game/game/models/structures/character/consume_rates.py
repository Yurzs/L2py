import dataclasses

from src.common.common.ctype import ctype


@dataclasses.dataclass(kw_only=True)
class ConsumeRates:
    mp: ctype.int32
    hp: ctype.int32
