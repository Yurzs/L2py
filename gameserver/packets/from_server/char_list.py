import typing

from common.datatypes import Int32, Int8
from common.helpers.bytearray import ByteArray
from common.packet import add_length
from gameserver.crypt.xor import xor_encrypt_game
from gameserver.models import Character
from .base import GameServerPacket


class CharList(GameServerPacket):
    type = Int8(19)

    def __init__(self, characters_list: typing.List[Character]):
        self.characters = characters_list

    @add_length
    @xor_encrypt_game
    def encode(self, client):
        arr = ByteArray(self.type.encode())
        arr.append(Int32(len(self.characters)))
        for character in self.characters:
            pass
        return arr
