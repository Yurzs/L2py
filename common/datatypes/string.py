from .base import DataType


class String(DataType):

    def encode(self):
        from common.helpers.bytearray import to_bytearray
        return to_bytearray((self.value + "\0").encode("ascii"))

    @classmethod
    def decode(cls, data):
        return cls(data.decode("ascii").replace("\0", ""))

    @classmethod
    def read(cls, data, start):
        from common.helpers.bytearray import ByteArray
        from common.datatypes.integer import UInt16

        pos = start
        string = ByteArray(b"")
        while pos < len(data):
            if UInt16(data[pos:pos + 2]) != 0:
                string += ByteArray(data[pos:pos + 2])
                pos += 2
            else:
                pos += 2
                break

        return cls(bytes(string).decode("utf-16")), pos
