from .base import DataType


class Float(DataType):
    length = 4
    struct_format = "f"

    def __float__(self):
        return float(self.value)


class Double(Float):
    length = 8
    struct_format = "d"
