import random

from common.keys.blowfish import BlowfishKey
from common.keys.rsa import L2RsaKey
from common.keys.xor import LoginXorKey
from .state import Connected


class LoginClient:
    def __init__(self, protocol):
        self.protocol = protocol
        self.state = Connected()
        self.rsa_key = L2RsaKey.generate()

        self.blowfish_key = BlowfishKey.generate()
        self.session_id = 12345
        # self.session_id = random.randrange(1, 2147483646)
        self.xor_key = LoginXorKey()
        self.session_id1 = None
        self.session_id2 = None
