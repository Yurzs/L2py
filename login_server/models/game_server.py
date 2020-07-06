from mdocument import Document

from login_server.config import database_name, mongo_client


class GameServer(Document):
    collection = "game_servers"
    database = database_name
    client = mongo_client
