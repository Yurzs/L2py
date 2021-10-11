from .base import DataType


class Bytes(DataType):
    def encode(self):
        from common.helpers.bytearray import to_bytearray

        return to_bytearray(self.value)

    @classmethod
    def decode(cls, data):
        return cls(data)

    def __bytes__(self):
        return self.value
