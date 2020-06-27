import random


class Account:

    @classmethod
    def generate_session_id(cls):
        return random.randrange(1, 0x7fffffff)
