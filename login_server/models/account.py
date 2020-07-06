import random

from mdocument import Document

from login_server.config import database_name, mongo_client


class Account(Document):
    collection = "accounts"
    database = database_name
    client = mongo_client

    @classmethod
    def generate_session_id(cls):
        return random.randrange(1, 0x7fffffff)

    @property
    def can_login(self):
        return True
