from mdocument import Document

from common.config import database, database_client


class Account(Document):
    collection = "accounts"
    database = database
    client = database_client
