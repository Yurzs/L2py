from common.datatypes import Int32


class LoginXorKey:
    def __init__(self, key=None):
        self.key = Int32.random() if not key else Int32(key)
        self.initiated = False

    def __repr__(self):
        return str(self.key)
