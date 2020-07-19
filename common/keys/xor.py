import random
import copy

from common.helpers.bytearray import ByteArray
from common.datatypes import Int32


class GameXorKey:
    def __init__(self):
        key = ByteArray(Int32.random())
        self.outgoing_key = key
        self.incoming_key = copy.deepcopy(key)


class LoginXorKey:
    def __init__(self, key=None):
        self.key = Int32.random() if not key else Int32(key)

    def __repr__(self):
        return str(self.key)
