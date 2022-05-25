import random

from common.ctype import ctype


class SessionKey:
    def __init__(
        self,
        login_ok1: ctype.int = None,
        login_ok2: ctype.int = None,
        play_ok1: ctype.int = None,
        play_ok2: ctype.int = None,
    ):
        self.login_ok1: ctype.int = (
            ctype.int.random() if login_ok1 is None else login_ok1
        )
        self.login_ok2: ctype.int = (
            ctype.int.random() if login_ok2 is None else login_ok2
        )

        self.login_ok2: ctype.int = (
            ctype.int.random() if login_ok2 is None else login_ok2
        )
        self.play_ok1: ctype.int = ctype.int.random() if play_ok1 is None else play_ok1
        self.play_ok2: ctype.int = ctype.int.random() if play_ok2 is None else play_ok2

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
