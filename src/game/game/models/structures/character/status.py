import dataclasses

from src.common.common.ctype import ctype
from src.common.common.dataclass import BaseDataclass


@dataclasses.dataclass(kw_only=True)
class Status(BaseDataclass):
    cp: ctype.int32 = 0
    hp: ctype.int32 = 0
    mp: ctype.int32 = 0

    weight_load: ctype.int32 = 0

    is_faking_death: ctype.bool = False
    is_in_combat: ctype.bool = False
    is_pvp: ctype.bool = False
    is_running: ctype.bool = False
    is_sitting: ctype.bool = False
    is_hero: ctype.bool = False
    is_noble: ctype.bool = False
    is_private_store: ctype.bool = False
    is_dwarf_craft_store: ctype.bool = False
    is_mounted: ctype.bool = False
    is_fishing: ctype.bool = False
    is_invulnerable: ctype.bool = False
    is_teleporting: ctype.bool = False
    is_betrayed: ctype.bool = False
    is_afraid: ctype.bool = False
    is_confused: ctype.bool = False
    is_flying: ctype.bool = False
    is_muted: ctype.bool = False
    is_physically_muted: ctype.bool = False
    is_dead: ctype.bool = False
    is_immobilized: ctype.bool = False
    is_overloaded: ctype.bool = False
    is_paralyzed: ctype.bool = False
    is_riding: ctype.bool = False
    is_pending_revive: ctype.bool = False
    is_rooted: ctype.bool = False
    is_sleeping: ctype.bool = False
    is_stunned: ctype.bool = False
