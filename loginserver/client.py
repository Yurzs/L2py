from common.datatypes import Int32
from common.keys.blowfish import BlowfishKey
from common.keys.rsa import L2RsaKey
from common.keys.xor import LoginXorKey
from common.keys.session import SessionKey
from .state import Connected


class LoginClient:
    def __init__(self, protocol):
        self.protocol = protocol
        self.state = Connected()
        self.rsa_key = L2RsaKey.generate()
        self.blowfish_key = BlowfishKey.generate()
        self.session_id = Int32.random()
        self.session_key = SessionKey()
        self.xor_key = LoginXorKey()
        self.protocol_version = 50721
