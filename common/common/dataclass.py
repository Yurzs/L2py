import dataclasses
import inspect
import types
import typing
from dataclasses import fields, is_dataclass

from typeguard import check_type

from common.ctype import ctype
from common.misc import classproperty


class BaseDataclass:
    @classmethod
    def __models__(cls):
        result = {}
        subclasses = BaseDataclass.__subclasses__()
        while subclasses:
            subclass = subclasses.pop()
            result[subclass.__name__] = subclass
            subclasses.extend(subclass.__subclasses__())

        return result

    def __setattr__(self, key, value):
        dataclass_fields = self._fields
        if key in dataclass_fields:
            field = dataclass_fields[key]
            try:
                check_type(field.name, value, field.type)
            except TypeError as e:
                e.args = (f"{e.args[0]} ({field.type.__name__})", *e.args[1:])
                raise e
            if isinstance(value, dict) and field.type in self.__models__().values():
                value = field.type(**value)
            elif hasattr(field.type, "__extra__") and not is_dataclass(field.type):
                value = field.type(value)
            elif isinstance(value, list) and isinstance(field.type, types.GenericAlias):
                list_items = []
                item_type = typing.get_args(field.type)[0]

                for item in value:
                    if isinstance(item, item_type):
                        list_items.append(item)
                    elif not dataclasses.is_dataclass(item_type):
                        list_items.append(item_type(item))
                    else:
                        list_items.append(item_type(**item))
                value = list_items
        super().__setattr__(key, value)

    def __post_init__(self):
        for field_name, field in self._fields.items():
            value = getattr(self, field_name)
            check_type(field_name, value, field.type)
            if isinstance(value, dict) and field.type in self.__models__():
                setattr(self, field_name, value)
            elif hasattr(field.type, "__extra__") and not is_dataclass(field.type):
                setattr(self, field_name, field.type(value))

    @classmethod
    def convert_dataclasses(cls, data: dict):
        result = {}
        models = cls.__models__()

        for field_name, field in cls._get_fields().items():
            value = data.get(field_name)
            if isinstance(value, dict) and field.type in models:
                model = models[field.type]
                result[field_name] = model(**model.convert_dataclasses(value))
            else:
                result[field_name] = value
        return result

    @property
    def _fields(self):
        return {field.name: field for field in fields(self)}

    @classmethod
    def _get_fields(cls):
        return {field.name: field for field in fields(cls)}

    def _get_field(self, field_name):
        return self._fields[field_name]

    def _get_field_type(self, field_name):
        try:
            return self._get_field(field_name).type
        except KeyError:
            if isinstance(getattr(self.__class__, field_name), property):
                signature = str(
                    inspect.signature(getattr(self.__class__, field_name).fget)
                )

                _, typehint = signature.split("->")
                typehint = typehint.strip()
                return typehint

            return type(getattr(self, field_name))

    def encode(self, strings_format="utf-16-le") -> bytearray:
        data = bytearray()
        models = self.__models__()

        for field_name in self.__encode__:
            field_type = self._get_field_type(field_name)
            value = getattr(self, field_name)

            if isinstance(field_type, str):
                if field_type.startswith("common.ctype."):
                    field_type = getattr(ctype, field_type.split(".")[-1])
                elif field_type in models.keys():
                    field_type = models[field_type]
                else:
                    field_type = eval(field_type, globals(), locals())

            if issubclass(field_type, BaseDataclass):
                data.extend(value.encode())
            elif isinstance(value, str):
                data.extend(value.encode(strings_format))
            else:
                data.extend(bytes(value))
        return data

    def to_dict(self):
        return dataclasses.asdict(self, dict_factory=encode_dataclass)

    @classproperty
    def __extra__(cls):
        return (cls, dict)


def encode_dataclass(dataclass_fields):
    from common.json import JsonEncoder

    result = {}

    encoder = JsonEncoder()
    for field, value in dataclass_fields:
        result[field] = encoder.encode(value)
    return result
