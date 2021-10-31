from dataclasses import dataclass, field

from common.dataclass import BaseDataclass
from game.models.structures.character.template import CharacterTemplateBase

#
# class ServerSide(BaseDataclass):
#     name:


class NpcTemplate(CharacterTemplateBase):
    id: Int32
    template_id: Int32
    type: UTFString
    name: UTFString
    server_side_name: Bool
    title: UTFString
    server_side_title: Bool
    sex: UTFString
    level: Int8
    reward_exp: Int32
    reward_sp: Int32
    aggro_range: Int32
    right_hand: Int32
    left_hand: Int32
    armor: Int32
    faction_id: UTFString
    faction_range: Int32
    absorb_level: Int32
    absorb_type: Int32
    race: Int32
