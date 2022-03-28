from dataclasses import dataclass, field

from common.dataclass import BaseDataclass
from common.helpers.cython import cython


@dataclass
class Status(BaseDataclass):
    cp: cython.long = 0
    hp: cython.long = 0
    mp: cython.long = 0

    weight_load: cython.long = 0

    is_faking_death: cython.bint = field(default=False)
    is_in_combat: cython.bint = field(default=False)
    is_pvp: cython.bint = field(default=False)
    is_running: cython.bint = field(default=False)
    is_sitting: cython.bint = field(default=False)
    is_hero: cython.bint = field(default=False)
    is_noble: cython.bint = field(default=False)
    is_private_store: cython.bint = field(default=False)
    is_dwarf_craft_store: cython.bint = field(default=False)
    is_mounted: cython.bint = field(default=False)
    is_fishing: cython.bint = field(default=False)
    is_invulnerable: cython.bint = field(default=False)
    is_teleporting: cython.bint = field(default=False)
    is_betrayed: cython.bint = field(default=False)
    is_afraid: cython.bint = field(default=False)
    is_confused: cython.bint = field(default=False)
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
