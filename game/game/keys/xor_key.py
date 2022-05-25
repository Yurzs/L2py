import copy
import random
import typing

from common.ctype import ctype


class GameXorKey:
    CRYPT_KEYS_COUNT = 20
    CRYPT_KEYS: typing.List[bytearray] = [bytearray(b"\x00" * 16) for _ in range(CRYPT_KEYS_COUNT)]

    for i in range(CRYPT_KEYS_COUNT):
        # for j in range(len(CRYPT_KEYS[i])):
        #     CRYPT_KEYS[i][j] = get_random(ctype.int8)

        CRYPT_KEYS[i][8]: ctype.int8 = 200
        CRYPT_KEYS[i][9]: ctype.int8 = 39
        CRYPT_KEYS[i][10]: ctype.int8 = 147
        CRYPT_KEYS[i][11]: ctype.int8 = 1
        CRYPT_KEYS[i][12]: ctype.int8 = 161
        CRYPT_KEYS[i][13]: ctype.int8 = 108
        CRYPT_KEYS[i][14]: ctype.int8 = 49
        CRYPT_KEYS[i][15]: ctype.int8 = 151

    def __init__(self):
        key = self.random_key()
        self.outgoing_key: bytearray = copy.deepcopy(key)
        self.incoming_key: bytearray = copy.deepcopy(key)

    @classmethod
    def random_key(cls) -> bytearray:
        return cls.CRYPT_KEYS[random.randrange(0, len(cls.CRYPT_KEYS))]
