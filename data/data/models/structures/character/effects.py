from dataclasses import dataclass, field

import common.datatypes
from common.dataclass import BaseDataclass


@dataclass
class Effects(BaseDataclass):
    is_afraid: common.datatypes.Bool = field(default=False)
    is_confused: common.datatypes.Bool = field(default=False)
    is_faking_death: common.datatypes.Bool = field(default=False)
    is_flying: common.datatypes.Bool = field(default=False)
    is_muted: common.datatypes.Bool = field(default=False)
    is_physically_muted: common.datatypes.Bool = field(default=False)
    is_dead: common.datatypes.Bool = field(default=False)
    is_immobilized: common.datatypes.Bool = field(default=False)
    is_overloaded: common.datatypes.Bool = field(default=False)
    is_paralyzed: common.datatypes.Bool = field(default=False)
    is_riding: common.datatypes.Bool = field(default=False)
    is_pending_revive: common.datatypes.Bool = field(default=False)
    is_rooted: common.datatypes.Bool = field(default=False)
    is_running: common.datatypes.Bool = field(default=False)
    is_sleeping: common.datatypes.Bool = field(default=False)
    is_stunned: common.datatypes.Bool = field(default=False)
    is_betrayed: common.datatypes.Bool = field(default=False)
    is_teleporting: common.datatypes.Bool = field(default=False)
    is_invulnerable: common.datatypes.Bool = field(default=False)
