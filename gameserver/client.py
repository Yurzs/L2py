from common.keys.xor import GameXorKey


class GameClient:
    def __init__(self, protocol):
        self.protocol = protocol
        self.xor_key = GameXorKey()
        # self.session_id =
