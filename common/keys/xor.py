import copy

from common.datatypes import Int32
from common.helpers.bytearray import ByteArray


class GameXorKey:
    def __init__(self, key=None):
        # key = ByteArray(b"\x00"*16)
        key = ByteArray.random(16) if not key else key
        self.outgoing_key = key
        self.incoming_key = copy.deepcopy(key)


class LoginXorKey:
    def __init__(self, key=None):
        self.key = Int32.random() if not key else Int32(key)

    def __repr__(self):
        return str(self.key)
