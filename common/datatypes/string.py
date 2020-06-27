from .base import DataType


class String(DataType):

    def encode(self):
        return self.data.encode("utf-8")

    @classmethod
    def decode(cls, data):
        return cls(data.decode("utf-8"))
