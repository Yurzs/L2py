from mdocument import Document

from loginserver.config import database_name, mongo_client


class GameServer(Document):
    """GameServer.

        structure = {
            "id": int,
            "ip": str,
            "port": int,
            "age_limit": int,
            "is_pvp": bool,
            "online": int,
            "max_online": int,
            "is_online": bool,
            "server_type": int,
            "public": bool,
            "brackets": bool,
        }

    """

    collection = "game_servers"
    database = database_name
    client = mongo_client

    @property
    def ip(self):
        ip = self._document_.get("ip", "127.0.0.1")
        if len(ip.split(".")) != 4:
            ip = "127.0.0.1"
        return [int(sip) for sip in ip.split(".")]

    @property
    def is_online(self):
        return bool(self._document_.get("is_online", False))
