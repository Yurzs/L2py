
from .state import Unauthenticated
from common.keys.blowfish import BlowfishKey


class Client:
    def __init__(self, protocol):
        self.protocol = protocol
        self.state = Unauthenticated()
        self.blowfish_key = BlowfishKey.generate()
