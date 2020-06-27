from .base import DataType


class Bytes(DataType):

    def encode(self):
        return self.data

    @classmethod
    def decode(cls, data):
        return cls(data)
