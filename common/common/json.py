import json
from typing import Any

import bson
import pymongo.results

from common.dataclass import _DATACLASS_MAP, BaseDataclass, TypedList


class JsonEncoder(json.JSONEncoder):
    def encode(self, o: Any):
        if isinstance(o, BaseDataclass):
            result = o.to_dict()
            result["$model"] = o.__class__.__name__.lower()
            return result
        elif isinstance(o, Int):
            return int(o)
        elif isinstance(o, bson.ObjectId):
            return {"$oid": str(o)}
        elif isinstance(o, TypedList):
            return list(o)
        elif isinstance(o, pymongo.results.InsertOneResult):
            return {
                "__insert_one_result__": {
                    "inserted_id": o.inserted_id,
                    "acknowledged": o.acknowledged,
                }
            }
        elif isinstance(o, pymongo.results.UpdateResult):
            return {
                "__update_result__": {
                    "raw_result": o.raw_result,
                    "acknowledged": o.acknowledged,
                }
            }
        return super().default(o)


class JsonDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, data):
        from common.models.account import Account  # noqa: F401
        from common.models.game_server import GameServer  # noqa: F401

        if isinstance(data, dict):
            if "$oid" in data:
                return bson.ObjectId(data["$oid"])
            elif "$model" in data:
                return _DATACLASS_MAP[data.pop("$model")](**data)
            elif "__insert_one_result__" in data:
                return pymongo.results.InsertOneResult(**data["__insert_one_result__"])
            elif "__update_result__" in data:
                return pymongo.results.UpdateResult(**data["__update_result__"])
        return data
