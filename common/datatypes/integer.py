from .base import DataType


class Int(DataType):
    length = 4
    struct_format = "i"

    def __eq__(self, other):
        return self.data == other


class Int64(Int):
    length = 8
    struct_format = "q"


class Short(Int):
    length = 4
    struct_format = "h"
