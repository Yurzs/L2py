from .base import DataType


class Char(DataType):
    length = 1
    struct_format = "c"

    def encode(self):
        if isinstance(self.data, int):
            return self.data.to_bytes(1, "big")
        else:
            return super().encode()
