from common.datatypes import Int32
from common.session import Session
from login.keys.blowfish import BlowfishKey
from login.keys.rsa import L2RsaKey
from login.keys.session import SessionKey
from login.keys.xor import LoginXorKey


class LoginSession(Session):
    def __init__(self, protocol):
        super().__init__()
        self.id = Int32.random()
        self.protocol = protocol
        self.state = None
        self.rsa_key = L2RsaKey.generate()
        self.blowfish_key = BlowfishKey.generate()
        self.session_key = SessionKey()
        self.xor_key = LoginXorKey()
        self.protocol_version = 50721
        self.blowfish_enabled = False

    @classmethod
    def by_username(cls, username):
        for session_id, session in cls.data().items():
            if session["account"].username == username:
                return {session_id: session}
