from src.common.common.ctype import ctype


class LoginXorKey:
    def __init__(self, key=None):
        self.key: ctype.int32 = ctype.int32.random() if not key else key
        self.initiated = False

    def __repr__(self):
        return str(self.key)
