import dataclasses
from dataclasses import field

from common.ctype import ctype
from common.dataclass import BaseDataclass


@dataclasses.dataclass(kw_only=True)
class Effects(BaseDataclass):
    is_afraid: ctype.bool = field(default=False)
    is_confused: ctype.bool = field(default=False)
    is_faking_death: ctype.bool = field(default=False)
    is_flying: ctype.bool = field(default=False)
    is_muted: ctype.bool = field(default=False)
    is_physically_muted: ctype.bool = field(default=False)
    is_dead: ctype.bool = field(default=False)
    is_immobilized: ctype.bool = field(default=False)
    is_overloaded: ctype.bool = field(default=False)
    is_paralyzed: ctype.bool = field(default=False)
    is_riding: ctype.bool = field(default=False)
    is_pending_revive: ctype.bool = field(default=False)
    is_rooted: ctype.bool = field(default=False)
    is_sleeping: ctype.bool = field(default=False)
    is_stunned: ctype.bool = field(default=False)
    is_betrayed: ctype.bool = field(default=False)
