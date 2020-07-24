from gameserver.keys.xor import GameXorKey
from loginserver.keys.blowfish import BlowfishKey
from gameserver.state import Connected


class GameClient:
    def __init__(self, protocol):
        self.state = Connected()
        self.protocol = protocol
        self.xor_key = GameXorKey()
        self.encryption_enabled = False
        self.blowfish_key = BlowfishKey.generate()
        self.session_id = None
        self.blowfish_enabled = False
