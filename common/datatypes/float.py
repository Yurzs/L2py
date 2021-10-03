from .base import DataType


class Float(DataType):
    length = 8
    struct_format = "d"

    def __float__(self):
        return float(self.value)
