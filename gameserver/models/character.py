from mdocument import Document

from gameserver.config import database_name, mongo_client


class Character(Document):
    collection = "characters"
    database = database_name
    client = mongo_client

