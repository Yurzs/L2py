from dataclasses import dataclass, field

from common.dataclass import BaseDataclass
from game.models.structures.character.template import CharacterTemplateBase

#
# class ServerSide(BaseDataclass):
#     name:


class NpcTemplate(CharacterTemplateBase):
    id: cython.long
    template_id: cython.long
    type: UTFString
    name: UTFString
    server_side_name: cython.bint
    title: UTFString
    server_side_title: cython.bint
    sex: UTFString
    level: cython.char
    reward_exp: cython.long
    reward_sp: cython.long
    aggro_range: cython.long
    right_hand: cython.long
    left_hand: cython.long
    armor: cython.long
    faction_id: UTFString
    faction_range: cython.long
    absorb_level: cython.long
    absorb_type: cython.long
    race: cython.long
