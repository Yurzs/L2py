from common.helpers.cython import cython

from .base import LoginServerPacket


class Reason:
    DATA_STEALER: cython.char = 1
    GENERIC_VIOLATION: cython.char = 8
    SEVEN_DAYS_PASSED: cython.char = 16
    ACCOUNT_BANNED: cython.char = 32


class AccountKicked(LoginServerPacket):
    type: cython.char = 2
    arg_order = ["type", "kick_reason"]

    REASON = Reason

    def __init__(self, kick_reason_id):
        self.kick_reason: cython.long = kick_reason_id
