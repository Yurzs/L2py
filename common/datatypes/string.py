from .base import DataType


class String(DataType):

    def encode(self):
        from common.helpers.bytearray import to_bytearray
        return to_bytearray((self.value + "\0").encode("ascii"))

    @classmethod
    def decode(cls, data):
        return cls(data.decode("ascii").replace("\0", ""))
