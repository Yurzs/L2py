import asyncio
import os
from functools import cached_property

import dotenv
from bson import ObjectId
from pydantic import Extra

from common.ctype import _CType, ctype
from common.misc import Singleton

dotenv.load_dotenv()


class Config(metaclass=Singleton):
    def __init__(self):
        self.loop = asyncio.get_event_loop()
        self.MONGO_URI = os.environ.get("MONGO_URI", "localhost")


class PydanticConfig:
    validate_all = True
    extra = Extra.forbid
    validate_assignment = True
    underscore_attrs_are_private = True
    arbitrary_types_allowed = True

    json_encoders = {
        ctype.char: lambda value: int.from_bytes(value.value, "big"),
        _CType: lambda value: value.value,
        ObjectId: lambda value: str(value),
    }
