import typing
from dataclasses import dataclass

from Cython.Shadow import typedef

from common.datatypes.base import DataType
from common.helpers.cython import convert_numeric_from_bytes, utf8str, utf16str


@dataclass
class Parameter:
    id: str
    start: typing.Union[int, str]
    type: type
    length: int = None
    func: typing.Optional[typing.Callable] = None
    stop: typing.Optional[int] = None

    def parse(self, data):
        if self.func is not None:
            return self.func(data)
        elif self.length is not None:
            if isinstance(self.type, typedef):
                return convert_numeric_from_bytes(self.type, data), self.length
            elif self.type in [utf8str, utf16str]:
                return self.type.decode(data), self.length
            elif hasattr(self.type, "decode"):
                return self.type.decode(data), self.length
            return self.type(data), self.length


class Template:
    def __init__(self, parameters: typing.List[Parameter]):
        self.template = {f"${parameter.id}": parameter for parameter in parameters.copy()}
        self.parameters = parameters

    def get_start(self, parameter_id):
        start = self.template[f"${parameter_id}"].start
        if isinstance(start, str):
            param_id, attr = start.split(".")
            return getattr(self.template[param_id], attr)
        return start

    def get_stop(self, parameter_id):
        stop = self.template[f"${parameter_id}"].stop
        if isinstance(stop, str):
            param_id, attr = stop.split(".")
            return getattr(self.template[param_id], attr)
        return stop

    def set_start(self, parameter_id, value):
        self.template[f"${parameter_id}"].start = value

    def set_stop(self, parameter_id, value):
        self.template[f"${parameter_id}"].stop = value
