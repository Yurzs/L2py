from .base import DataType


class Float(DataType):
    length = 4
    struct_format = "f"

    def __float__(self):
        return float(self.value)

    def __mul__(self, other):
        if isinstance(other, Float):
            return self.value * other.value
        else:
            return self.value * other


class Double(Float):
    length = 8
    struct_format = "d"
    prefix = ""
