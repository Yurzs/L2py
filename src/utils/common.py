import decimal
import json
import re
import string
import typing

camel_case_pattern = re.compile(r"(?<!^)(?<![A-Z])(?=[A-Z])")


class JsonEncoder(json.JSONEncoder):
    def _inner_list(self, data: list):
        for item in data:
            if isinstance(item, dict):
                self._inner_dict(item)
            if isinstance(item, list):
                self._inner_list(item)

    def _inner_dict(self, data: dict):
        for key, value in data.copy().items():
            snake_case_key = camel_case_pattern.sub("_", key).lower().replace("__", "_")
            snake_case_key = (
                snake_case_key[1:] if snake_case_key.startswith("_") else snake_case_key
            )
            if isinstance(value, dict):
                if len(value) == 1 and list(value.keys())[0] in ["val"]:
                    self._inner_dict(value)
                    data[list(value.keys())[0]] = value[list(value.keys())[0]]
                    if key != snake_case_key:
                        del data[key]
                    continue
                self._inner_dict(value)
            elif isinstance(value, list):
                self._inner_list(value)
            elif isinstance(value, str):
                value = value.strip().replace("\n", "")
                if value.isnumeric():
                    value = int(value)
                elif value.startswith("0x"):
                    value = int(value, 16)
                elif all(c in string.digits + " -" for c in value) and len(value) > 0:
                    value = [int(val) for val in value.split(" ") if len(val) > 0]
                elif all(c in string.digits + " -." for c in value) and len(value) > 0:
                    value = [float(val) for val in value.split(" ") if len(val) > 0]
                elif value == "none":
                    value = None
                elif value == "false":
                    value = False
                elif value == "true":
                    value = True
                if isinstance(value, list) and len(value) == 1:
                    value = value[0]
            elif isinstance(value, decimal.Decimal):
                if value % 1 == 0:
                    value = int(value)
                else:
                    value = float(value)

            data[snake_case_key.replace("for", "action")] = value

            if key != snake_case_key.replace("for", "action"):
                del data[key]

    def encode(self, o: typing.Any) -> str:
        if isinstance(o, typing.Mapping):
            self._inner_dict(o)
        if isinstance(o, list):
            self._inner_list(o)
        return super().encode(o)
