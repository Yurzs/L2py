import copy
import os
import random

from common.datatypes import Int8
from common.helpers.bytearray import ByteArray


class GameXorKey:
    CRYPT_KEYS_COUNT = 20
    CRYPT_KEYS = [ByteArray(b"0" * 16) for _ in range(CRYPT_KEYS_COUNT)]

    for i in range(CRYPT_KEYS_COUNT):
        for j in range(len(CRYPT_KEYS[i])):
            CRYPT_KEYS[i][j] = Int8.random()

        CRYPT_KEYS[i][8] = Int8(200)
        CRYPT_KEYS[i][9] = Int8(39)
        CRYPT_KEYS[i][10] = Int8(147)
        CRYPT_KEYS[i][11] = Int8(1)
        CRYPT_KEYS[i][12] = Int8(161)
        CRYPT_KEYS[i][13] = Int8(108)
        CRYPT_KEYS[i][14] = Int8(49)
        CRYPT_KEYS[i][15] = Int8(151)

    def __init__(self):
        key = self.random_key()
        self.outgoing_key = copy.deepcopy(key)
        self.incoming_key = copy.deepcopy(key)

    @classmethod
    def random_key(cls):
        return cls.CRYPT_KEYS[random.randrange(0, len(cls.CRYPT_KEYS))]
