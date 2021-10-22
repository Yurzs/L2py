from dataclasses import dataclass, field

from common.dataclass import BaseDataclass


@dataclass
class Status(BaseDataclass):
    cp: Int32 = 0
    hp: Int32 = 0
    mp: Int32 = 0

    is_faking_death: Bool = field(default=False)
    is_in_combat: Bool = field(default=False)
    is_pvp: Bool = field(default=False)
    is_running: Bool = field(default=False)
    is_sitting: Bool = field(default=False)
    is_hero: Bool = field(default=False)
    is_noble: Bool = field(default=False)
    is_private_store: Bool = field(default=False)
    is_dwarf_craft_store: Bool = field(default=False)
    is_mounted: Bool = field(default=False)
    is_fishing: Bool = field(default=False)
    is_invulnerable: Bool = field(default=False)
    is_teleporting: Bool = field(default=False)
    is_betrayed: Bool = field(default=False)
    is_afraid: Bool = field(default=False)
    is_confused: Bool = field(default=False)
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
