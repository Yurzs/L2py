from typing import ClassVar, _GenericAlias

from pydantic import BaseModel as PydanticBaseModel
from pydantic.main import ModelMetaclass as PydanticModelMetaclass

from common.config import PydanticConfig
from common.ctype import _Bool, _Char, _Float, _Integer
from common.misc import extend_bytearray


class ModelMetaclass(PydanticModelMetaclass):
    def __new__(mcs, name, bases, namespace, **kwargs):
        # Convert ClassVar values
        for field_name, field_annotation in namespace.get("__annotations__", {}).items():
            if not issubclass(type(field_annotation), _GenericAlias):
                continue

            if not hasattr(field_annotation, "__origin__"):
                continue

            if field_annotation.__origin__ == ClassVar and namespace.get(field_name) is not None:
                field_type = field_annotation.__args__[0]

                if isinstance(namespace[field_name], field_type):
                    continue

                try:
                    namespace[field_name] = field_type(namespace[field_name])
                except Exception as e:
                    raise ValueError(f"Invalid value for {field_name}: {e}") from None

        return super().__new__(mcs, name, bases, namespace, **kwargs)


class BaseModel(PydanticBaseModel, metaclass=ModelMetaclass):
    class Config(PydanticConfig):
        pass

    def dict(self, *args, **kwargs):
        by_alias = kwargs.pop("by_alias", True)
        exclude_none = kwargs.pop("exclude_none", True)
        exclude_defaults = kwargs.pop("exclude_defaults", True)
        # exclude_unset = kwargs.pop("exclude_unset", True)

        result = super().dict(
            *args,
            **kwargs,
            by_alias=by_alias,
            exclude_none=exclude_none,
            exclude_defaults=exclude_defaults,
            # exclude_unset=exclude_unset,
        )

        def convert_value(field_type, value):
            if issubclass(field_type, _Float):
                return float(value.value)
            elif issubclass(field_type, _Char):
                return int.from_bytes(value, "big")
            elif issubclass(field_type, _Bool):
                return bool(value)
            elif issubclass(field_type, _Integer):
                return int(value)
            return value

        for field in self.__fields__.values():
            if result.get(field.alias) is None:
                continue

            if field.type_ != field.outer_type_:
                # GenericAlias
                origin_type = field.outer_type_.__origin__

                if field.outer_type_.__origin__ not in [list, tuple, set, dict]:
                    result[field.alias] = convert_value(field.type_, result[field.alias])
                    continue

                inner_type = field.type_
                if origin_type in (list, tuple, set):
                    result[field.alias] = origin_type(
                        [convert_value(inner_type, item) for item in result[field.alias]]
                    )
                elif origin_type == dict:
                    key_type, value_type = inner_type.__args__
                    result[field.alias] = {
                        convert_value(key_type, key): convert_value(value_type, value)
                        for key, value in result[field.alias].items()
                    }
            else:
                result[field.alias] = convert_value(field.type_, result[field.alias])

        return result

    def encode(self, include: list[str] = None, strings_format="utf-8") -> bytearray:
        """Encode model to bytearray.

        :param include: list of fields (attributes) to include.
            By default, only model fields are included.
            Pass properties names to include them.
            Order of fields/attributes is used to encode fields.
        :param strings_format: strings encoding format utf-8 / utf-16-le (default: utf-8).
        :return: encoded bytearray
        """

        encoded = bytearray()

        extension = []
        for field in include or self.__fields__:
            value = getattr(self, field)

            if isinstance(value, BaseModel):
                extension.append(value.encode(strings_format=strings_format))
            elif isinstance(value, str):
                extension.append(value.encode(strings_format))
            else:
                extension.append(value)

        extend_bytearray(encoded, extension)

        return encoded
