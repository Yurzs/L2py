from typing import ClassVar

from common.ctype import ctype
from common.misc import encode_str, extend_bytearray
from common.model import BaseModel
from game.models.character import Character
from game.packets.base import GameServerPacket


class FormattedCharacter(BaseModel):
    name: str
    id: ctype.int32
    account_username: str
    session_id: ctype.int32
    clan_id: ctype.int32
    unknown1: ctype.int32
    sex: ctype.int32
    race: ctype.int32
    active_class: ctype.int32


class CharList(GameServerPacket):
    type: ctype.int8 = 19
    characters: list[Character] = ()

    def encode(self, session):
        account = session.account
        encoded: bytearray = bytearray(self.type)
        encoded.extend(ctype.int32(len(self.characters)))

        for character in self.characters:
            extend_bytearray(
                encoded,
                [
                    encode_str(character.name),
                    character.id,
                    encode_str(account.username),
                    session.id,
                    ctype.int32(0),  # TODO: clan_id,
                    ctype.int32(0),
                    ctype.int32(character.appearance.sex),
                    character.race,
                    character.active_class,
                    character.active,
                    character.position.point3d.x,
                    character.position.point3d.y,
                    character.position.point3d.z,
                    ctype.double(character.status.hp),
                    ctype.double(character.status.mp),
                    character.stats.sp,
                    character.stats.exp,
                    character.stats.level,
                    character.karma,
                    character.pk_kills,
                    character.pvp_kills,
                    *[ctype.int32(0) for _ in range(7)],
                    *character.inventory.encode(),
                    character.appearance.hair_style,
                    character.appearance.hair_color,
                    character.appearance.face_id,
                    ctype.double(character.stats.max_hp),
                    ctype.double(character.stats.max_mp),
                    character.time_until_deletion,
                    character.active_class,
                    ctype.int32(account.last_character == character.name),
                    ctype.int8(0),
                    character.appearance.face_id,
                ],
            )
        return encoded


template = {
    "type": ctype.int8,
    "count": ctype.int32,
    "characters": [
        {
            "name": str,
            "id": ctype.int32,
            "login_name": str,
            "session_id": ctype.int32,
            "clan_id": ctype.int32,
            "skip1": ctype.int32,
            "sex": ctype.int32,
            "class_id": ctype.int32,
            "active": ctype.int32,
            "x": ctype.int32,
            "y": ctype.int32,
            "z": ctype.int32,
            "cur_hp": ctype.float,
            "cur_mp": ctype.float,
            "sp": ctype.int32,
            "exp": ctype.uint64,
            "level": ctype.int32,
            "karma": ctype.int32,
            "skip2": ctype.int64,
            "skip3": ctype.int64,
            "skip4": ctype.int64,
            "skip5": ctype.int64,
            "skip6": ctype.int32,
            "under": ctype.int32,
            "right_ear": ctype.int32,
            "left_ear": ctype.int32,
            "neck": ctype.int32,
            "right_finger": ctype.int32,
            "left_finger": ctype.int32,
            "head": ctype.int32,
            "right_hand": ctype.int32,
            "left_hand": ctype.int32,
            "gloves": ctype.int32,
            "chest": ctype.int32,
            "legs": ctype.int32,
            "feet": ctype.int32,
            "back": ctype.int32,
            "double_hand": ctype.int32,
            "hair": ctype.int32,
            "face": ctype.int32,
            "under2": ctype.int32,
            "right_ear2": ctype.int32,
            "left_ear2": ctype.int32,
            "neck2": ctype.int32,
            "right_finger2": ctype.int32,
            "left_finger2": ctype.int32,
            "head2": ctype.int32,
            "right_hand2": ctype.int32,
            "left_hand2": ctype.int32,
            "gloves2": ctype.int32,
            "chest2": ctype.int32,
            "legs2": ctype.int32,
            "feet2": ctype.int32,
            "back2": ctype.int32,
            "double_hand2": ctype.int32,
            "hair2": ctype.int32,
            "face2": ctype.int32,
            "max_hp": ctype.float,
            "max_mp": ctype.float,
            "days_left": ctype.int32,
            "class_id": ctype.int32,
            "enchant_effect": ctype.bool,
        }
    ],
}
