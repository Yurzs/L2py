from common.ctype import ctype
from game.models.structures.character.template import CharacterTemplate


class NpcTemplate(CharacterTemplate):
    id: ctype.int32
    template_id: ctype.int32
    type: str
    name: str
    server_side_name: ctype.bool
    title: str
    server_side_title: ctype.bool
    sex: str
    level: ctype.int8
    reward_exp: ctype.int32
    reward_sp: ctype.int32
    aggro_range: ctype.int32
    right_hand: ctype.int32
    left_hand: ctype.int32
    armor: ctype.int32
    faction_id: str
    faction_range: ctype.int32
    absorb_level: ctype.int32
    absorb_type: ctype.int32
    race: ctype.int32
