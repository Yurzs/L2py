from dataclasses import dataclass, field

from common.dataclass import BaseDataclass


@dataclass
class Effects(BaseDataclass):
    is_afraid: Bool = field(default=False)
    is_confused: Bool = field(default=False)
    is_faking_death: Bool = field(default=False)
    is_flying: Bool = field(default=False)
    is_muted: Bool = field(default=False)
    is_physically_muted: Bool = field(default=False)
    is_dead: Bool = field(default=False)
    is_immobilized: Bool = field(default=False)
    is_overloaded: Bool = field(default=False)
    is_paralyzed: Bool = field(default=False)
    is_riding: Bool = field(default=False)
    is_pending_revive: Bool = field(default=False)
    is_rooted: Bool = field(default=False)
    is_sleeping: Bool = field(default=False)
    is_stunned: Bool = field(default=False)
    is_betrayed: Bool = field(default=False)
