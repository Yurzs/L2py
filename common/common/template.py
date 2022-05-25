from __future__ import annotations

import copy
import typing
from dataclasses import dataclass

from common.request import Request


@dataclass(kw_only=True)
class Parameter:
    id: str
    start: typing.Union[int, str]
    type: typing.Union[type, Template]
    length: int = None
    func: typing.Optional[typing.Callable] = None
    stop: typing.Optional[int] = None
    repeat: typing.Union[str, int] = None

    def parse(self, data, namespace):
        if self.repeat is None:
            repeat_count = 1
        else:
            repeat_count = self.repeat if isinstance(self.repeat, int) else namespace[self.repeat]

        result = []
        total_len = 0

        for _ in range(int(repeat_count)):
            param_len = 0
            if isinstance(self.type, Template):
                template = copy.deepcopy(self.type)
                value = template.parse_request(data[total_len:])
                param_len = template.parameters[-1].stop

            elif self.func is not None:
                value, param_len = self.func(data[total_len:])

            elif self.length is not None:
                if hasattr(self.type, "decode"):
                    value, param_len = self.type.decode(data[total_len:]), self.length
                else:
                    value, param_len = self.type(data[total_len:]), self.length
            total_len += param_len
            result.append(value)
        return result[0] if self.repeat is None else result, total_len


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

    def parse_request(self, data: bytearray):
        result = {}

        for parameter in self.parameters:
            start = self.get_start(parameter.id)
            if parameter.length is not None:
                chunk = bytearray(data[start : start + parameter.length])
            elif parameter.stop is not None:
                chunk = bytearray(data[start : parameter.stop])
            else:
                chunk = bytearray(data[start:])
            parsed_value, stop = parameter.parse(
                chunk, namespace={f"${key}": value for key, value in result.items()}
            )
            self.set_stop(parameter.id, start + stop)
            result[parameter.id] = parsed_value
        return result
