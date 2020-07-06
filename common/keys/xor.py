import random

from common.helpers.bytearray import ByteArray


class GameXorKey:
    def __init__(self):
        key = ByteArray(random.randrange(1, 2147483646))
        self.encrypt_key = key
        self.decrypt_key = key


class LoginXorKey:
    def __init__(self):
        self.key = 12345
        # self.key = random.randrange(1, 2147483646)
