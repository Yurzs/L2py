import collections
import copy
import dataclasses
import sys
import typing
from typing import get_args, get_origin

_DATACLASS_MAP = {}


def post_init_inheritance(dataclass_instance):
    def find_bases(search_bases):
        found = set()
        for search_base in search_bases:
            if hasattr(search_base, "__post_init__"):
                if search_base.__post_init__ is not post_init_inheritance:
                    found.add(search_base)
                    continue
                parent_bases = find_bases(search_base.__bases__)
                if parent_bases:
                    found.update(parent_bases)
        return found

    for base in find_bases(dataclass_instance.__class__.__bases__):
        base.__post_init__(dataclass_instance)


class TypedList(collections.UserList):
    def __init__(self, items_type, iterable=()):
        self.items_type = items_type
        for item_n, item in enumerate(copy.copy(iterable)):
            if isinstance(item, int) and issubclass(self.items_type, Int):
                iterable[item_n] = self.items_type(item)
            elif not isinstance(item, self.items_type):
                raise ValueError(f"Wrong item type {type(item)}.")
        super().__init__(iterable)

    def append(self, item) -> None:
        if not isinstance(item, self.items_type):
            raise ValueError("Wrong item type.")
        return super().append(item)

    def insert(self, i: int, item) -> None:
        if not isinstance(item, self.items_type):
            raise ValueError("Wrong item type.")
        return super().insert(i, item)

    def __add__(self, other):
        if isinstance(other, (TypedList, self.items_type)):
            return super().__add__(other)
        raise ValueError("Wrong item type.")


class MetaBaseDataclass(type):
    def __new__(mcs, name, bases, namespace):
        if bases:
            if "__post_init__" not in namespace:
                namespace["__post_init__"] = post_init_inheritance
        return super().__new__(mcs, name, bases, namespace)


@dataclasses.dataclass
class BaseDataclass(metaclass=MetaBaseDataclass):
    HOOK_VALIDATE = "validate"
    ALL_HOOKS = [HOOK_VALIDATE]
    __hooks = collections.defaultdict(lambda: collections.defaultdict(list))

    @property
    def _fields(self):
        return {field.name: field for field in dataclasses.fields(self)}

    def _get_field(self, field_name):
        return self._fields[field_name]

    @staticmethod
    def _ensure_special_container(field, field_value):
        if not isinstance(field_value, (list, set, TypedList)):
            raise ValueError(f"Wrong value type for {field.name}.")
        items_type = field.type.__args__[0]
        if issubclass(items_type, typing.List):
            field_value = TypedList(items_type, field_value)
        else:
            for item_n, item in enumerate(field_value.copy()):
                if isinstance(item, items_type):
                    field_value[item_n] = item
                else:
                    field_value[item_n] = items_type(item)
        return field_value

    @staticmethod
    def _ensure_special_dict(field, field_value):
        if not isinstance(field_value, dict):
            raise ValueError(f"Wrong value type for {field.name}.")
        k_type, v_type = field.type.__args__
        new_dict = {}
        for key, value in field_value.items():
            new_dict[k_type(key)] = v_type(value)
        return new_dict

    @classmethod
    def ensure_field_value(cls, field, field_value):
        """Ensures that value matches provided typehint."""

        if field.default is None and field_value is None:
            return None
        elif (
            isinstance(field.type, type)
            and issubclass(field.type, BaseDataclass)
            and isinstance(field_value, dict)
        ):
            return field.type(**field_value)
        elif isinstance(field.type, typing._GenericAlias):
            if get_origin(field.type) in [list, set, frozenset]:
                return cls._ensure_special_container(field, field_value)
            elif get_origin(field.type) is dict:
                return cls._ensure_special_dict(field, field_value)
            elif get_origin(field.type) is typing.Union:
                if not isinstance(field_value, get_args(field.type)):
                    raise ValueError(f"Wrong value type for {field.name}.")
                return field_value
        if isinstance(field_value, field.type):
            return field_value
        return field.type(field_value)

    def __post_init__(self):
        for field_name, field in self.__class__.__dataclass_fields__.items():
            setattr(
                self,
                field_name,
                self.ensure_field_value(field, getattr(self, field_name)),
            )
        for cls, hooks in self.__hooks.items():
            if issubclass(self.__class__, cls):
                for func in hooks[self.HOOK_VALIDATE]:
                    func(self)

    @classmethod
    def hooks_parser(cls):
        for key, value in cls.__dict__.items():
            if any(map(lambda hook_name: key.startswith(hook_name), cls.ALL_HOOKS)):
                hook_name = key.split("_")[0]
                cls.__hooks[cls][hook_name] = value

    def __setattr__(self, key, value):
        if key in self._fields:
            field = self._get_field(key)
            return super().__setattr__(key, self.ensure_field_value(field, value))
        raise AttributeError()

    def to_dict(self):
        """Returns dictionary representation of dataclass."""

        def convert_object(value):
            if isinstance(value, Int):
                return int(value)
            elif isinstance(value, String):
                return str(value)
            elif isinstance(value, Bytes):
                return bytes(value)
            elif isinstance(value, Float):
                return float(value)
            elif isinstance(value, dict):
                return custom_data_types_dict_factory(value.items())
            elif isinstance(value, (list, set, frozenset, tuple)):
                result = []
                for item in value:
                    result.append(convert_object(item))
                return type(value)(result)
            else:
                return value

        def custom_data_types_dict_factory(key_value_tuple):
            result = {}
            for key, value in key_value_tuple:
                if key.startswith("__"):
                    continue
                result[key] = convert_object(value)
            return result

        return dataclasses.asdict(self, dict_factory=custom_data_types_dict_factory)

    def __init_subclass__(cls, **kwargs):
        _DATACLASS_MAP[cls.__name__.lower()] = cls
        cls.hooks_parser()

    @classmethod
    def update_forward_refs(cls, **localns):
        globalns = sys.modules[cls.__module__].__dict__.copy()
        globalns.setdefault(cls.__name__, cls)
        for f in cls.__dataclass_fields__.values():
            cls._update_field_forward_refs(f, globalns=globalns, localns=localns)

    @staticmethod
    def _update_field_forward_refs(
        field: "ModelField", globalns: typing.Any, localns: typing.Any
    ) -> None:
        """
        Try to update ForwardRefs on fields based on this ModelField, globalns and localns.
        """

        if field.type.__class__ == typing.ForwardRef:
            field.type = field.type._eval_type(globalns, localns) or None
            field.prepare()
        elif field.type.__class__ == str:
            field.type = eval(field.type, globalns, localns)
