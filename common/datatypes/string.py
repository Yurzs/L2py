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

        buf = ByteArray(b"")
        pos = start
        while pos < len(data):
            if data[pos] != 0:
                buf.append(data[pos])
                pos +=1
            else:
                break
        return cls.decode(bytes(buf)), pos
