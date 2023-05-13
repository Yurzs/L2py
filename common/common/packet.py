from abc import abstractmethod

from common.ctype import ctype
from common.model import BaseModel


class Packet(BaseModel):
    type: ctype.int8

    @abstractmethod
    def encode(self, session, strings_format="utf-8"):
        return super().encode(strings_format=strings_format)

    @classmethod
    @abstractmethod
    def parse(cls, data, client):
        pass

    @classmethod
    @abstractmethod
    def decode(cls, data, client, **kwargs):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"
