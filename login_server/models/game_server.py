import random
from mdocument import Document
from login_server.config import mongo_client, database_name


class GameServer(Document):
    collection = "game_servers"
    database = database_name
    client = mongo_client
