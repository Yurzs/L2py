from common.datatypes import Int32
from loginserver.keys.blowfish import BlowfishKey
from loginserver.keys.rsa import L2RsaKey
from loginserver.keys.xor import LoginXorKey
from loginserver.keys.session import SessionKey
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
        self.blowfish_key.decode = True
        self.blowfish_enabled = True
        self.encryption_enabled = True
