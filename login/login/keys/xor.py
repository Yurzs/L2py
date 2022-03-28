import cython

import common.helpers.cython


class LoginXorKey:
    def __init__(self, key=None):
        self.key: cython.int = common.helpers.cython.get_random(cython.int) if not key else key
        self.initiated = False

    def __repr__(self):
        return str(self.key)
