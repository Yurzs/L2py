from mdocument import Document

from gameserver.config import database_name, mongo_client


class Character(Document):
    collection = "characters"
    database = database_name
    client = mongo_client

    @classmethod
    def create(cls, **kwargs) -> "Document":
        query = {
            "name": kwargs["name"],
            "char_id": "",
            "account": kwargs["account"],
            "clan_id": kwargs.get("clan_id"),
            "sex": kwargs["sex"],
            "race": kwargs["race"],
            "base_class_id": kwargs["base_class_id"],
            "pos_x": kwargs["pos_x"],
            "pos_y": kwargs["pos_y"],
            "pos_z": kwargs["pos_z"],
            "hp": kwargs["hp"],
            "mp": kwargs["mp"],
            "sp": kwargs["sp"],
            "exp": kwargs.get("exp", 0),
            "lvl": kwargs.get("lvl", 1),
            "karma": kwargs.get("karma", 0),
        }
