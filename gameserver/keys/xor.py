import copy
import os

from common.datatypes import Int8
from common.helpers.bytearray import ByteArray


class GameXorKey:
    def __init__(self, key=None):
        key = self.generate_game_key() if not key else key
        self.outgoing_key = key
        self.incoming_key = copy.deepcopy(key)

    @classmethod
    def generate_game_key(cls):
        key = ByteArray(os.urandom(8))
        key.append(Int8(0xc8))
        key.append(Int8(0x27))
        key.append(Int8(0x93))
        key.append(Int8(0x01))
        key.append(Int8(0xa1))
        key.append(Int8(0x6c))
        key.append(Int8(0x31))
        key.append(Int8(0x97))
        return key