from dataclasses import dataclass, field

import common.datatypes
from common.dataclass import BaseDataclass
from data.models.structures.character.template import CharacterTemplateBase


class NpcTemplate(CharacterTemplateBase):
    id: common.datatypes.Int32
    template_id: common.datatypes.Int32
    type: common.datatypes.UTFString
    name: common.datatypes.UTFString
    server_side_name: common.datatypes.Bool
    title: common.datatypes.UTFString
    server_side_title: common.datatypes.Bool
    sex: common.datatypes.UTFString
    level: common.datatypes.Int8
    reward_exp: common.datatypes.Int32
    reward_sp: common.datatypes.Int32
    aggro_range: common.datatypes.Int32
    right_hand: common.datatypes.Int32
    left_hand: common.datatypes.Int32
    armor: common.datatypes.Int32
    faction_id: common.datatypes.UTFString
    faction_range: common.datatypes.Int32
    absorb_level: common.datatypes.Int32
    absorb_type: common.datatypes.Int32
    race: common.datatypes.Int32
