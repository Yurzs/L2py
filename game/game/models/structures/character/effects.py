from common.ctype import ctype
from common.model import BaseModel


class Effects(BaseModel):
    is_afraid: ctype.bool = False
    is_confused: ctype.bool = False
    is_faking_death: ctype.bool = False
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
    is_betrayed: ctype.bool = False
