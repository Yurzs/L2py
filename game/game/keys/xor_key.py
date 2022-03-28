import copy
import random

from common.helpers.bytearray import ByteArray


class GameXorKey:
    CRYPT_KEYS_COUNT = 20
    CRYPT_KEYS = [ByteArray(b"0" * 16) for _ in range(CRYPT_KEYS_COUNT)]

    for i in range(CRYPT_KEYS_COUNT):
        for j in range(len(CRYPT_KEYS[i])):
            CRYPT_KEYS[i][j] = cython.char.random()

        CRYPT_KEYS[i][8] = cython.char(200)
        CRYPT_KEYS[i][9] = cython.char(39)
        CRYPT_KEYS[i][10] = cython.char(147)
        CRYPT_KEYS[i][11] = cython.char(1)
        CRYPT_KEYS[i][12] = cython.char(161)
        CRYPT_KEYS[i][13] = cython.char(108)
        CRYPT_KEYS[i][14] = cython.char(49)
        CRYPT_KEYS[i][15] = cython.char(151)

    def __init__(self):
        key = self.random_key()
        self.outgoing_key = copy.deepcopy(key)
        self.incoming_key = copy.deepcopy(key)

    @classmethod
    def random_key(cls):
        return cls.CRYPT_KEYS[random.randrange(0, len(cls.CRYPT_KEYS))]
