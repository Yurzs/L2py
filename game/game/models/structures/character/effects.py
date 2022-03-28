from dataclasses import dataclass, field

from common.dataclass import BaseDataclass


@dataclass
class Effects(BaseDataclass):
    is_afraid: cython.bint = field(default=False)
    is_confused: cython.bint = field(default=False)
    is_faking_death: cython.bint = field(default=False)
    is_flying: cython.bint = field(default=False)
    is_muted: cython.bint = field(default=False)
    is_physically_muted: cython.bint = field(default=False)
    is_dead: cython.bint = field(default=False)
    is_immobilized: cython.bint = field(default=False)
    is_overloaded: cython.bint = field(default=False)
    is_paralyzed: cython.bint = field(default=False)
    is_riding: cython.bint = field(default=False)
    is_pending_revive: cython.bint = field(default=False)
    is_rooted: cython.bint = field(default=False)
    is_sleeping: cython.bint = field(default=False)
    is_stunned: cython.bint = field(default=False)
    is_betrayed: cython.bint = field(default=False)
