import random
import copy

from common.helpers.bytearray import ByteArray


class GameXorKey:
    def __init__(self):
        key = ByteArray(random.randrange(1, 2147483646))
        self.outgoing_key = key
        self.incoming_key = copy.deepcopy(key)


class LoginXorKey:
    def __init__(self):
        self.key = random.randrange(1, 2147483646)
