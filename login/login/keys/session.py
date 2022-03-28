import random

from common.helpers.cython import cython, get_random


class SessionKey:
    def __init__(
        self,
        login_ok1: cython.long = None,
        login_ok2: cython.long = None,
        play_ok1: cython.long = None,
        play_ok2: cython.long = None,
    ):
        self.login_ok1: cython.long = get_random(cython.long) if login_ok1 is None else login_ok1
        self.login_ok2: cython.long = get_random(cython.long) if login_ok2 is None else login_ok2
        self.login_ok2: cython.long = (
            cython.long(random.randrange(0, 2 ** 64)) if login_ok2 is None else login_ok2
        )
        self.play_ok1: cython.long = get_random(cython.long) if play_ok1 is None else play_ok1
        self.play_ok2: cython.long = get_random(cython.long) if play_ok2 is None else play_ok2

    def __eq__(self, other):
        if isinstance(other, SessionKey):
            if (
                self.login_ok1 == other.login_ok1
                and self.login_ok2 == other.login_ok2
                and self.play_ok1 == other.play_ok1
                and self.play_ok2 == other.play_ok2
            ):
                return True
        else:
            return False

    def verify_login(self, login_ok1, login_ok2):
        """Verifies that login session match."""

        if self.login_ok1 == login_ok1 and self.login_ok2 == login_ok2:
            return True
        return False

    def to_dict(self):
        return {
            "login_ok1": self.login_ok1,
            "login_ok2": self.login_ok2,
            "play_ok1": self.play_ok1,
            "play_ok2": self.play_ok2,
        }
