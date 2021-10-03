import dataclasses
import typing

import common.datatypes

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


class MetaBaseDataclass(type):
    def __new__(mcs, name, bases, namespace):
        if bases:
            if "__post_init__" not in namespace:
                namespace["__post_init__"] = post_init_inheritance
        return super().__new__(mcs, name, bases, namespace)


@dataclasses.dataclass
class BaseDataclass(metaclass=MetaBaseDataclass):
    @property
    def _fields(self):
        return {field.name: field for field in dataclasses.fields(self)}

    def _get_field(self, field_name):
        return self._fields[field_name]

    @classmethod
    def ensure_field_value(cls, field, field_value):
        """Validates that value matches provided typehint."""

        if field.default is None and field_value is None:
            return None
        elif isinstance(field.type, typing._GenericAlias):
            if field.type.__origin__ in [list, set, frozenset]:
                if not isinstance(field_value, (list, set, tuple)):
                    raise ValueError(f"Wrong value type for {field.id}.")
                items_type = field.type.__args__[0]
                for item_n, item in enumerate(field_value.copy()):
                    if isinstance(item, items_type):
                        field_value[item_n] = item
                    else:
                        field_value[item_n] = items_type(item)
                return field_value
            elif field.type.__origin__ is dict:
                if not isinstance(field_value, dict):
                    raise ValueError(f"Wrong value type for {field.name}.")
                k_type, v_type = field.type.__args__
                new_dict = {}
                for key, value in field_value.items():
                    new_dict[k_type(key)] = v_type(value)
                return new_dict
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

    def __setattr__(self, key, value):
        if key in self._fields:
            field = self._get_field(key)
            return super().__setattr__(key, self.ensure_field_value(field, value))
        raise AttributeError()

    def to_dict(self):
        """Returns dictionary representation of dataclass."""

        def custom_data_types_dict_factory(key_value_tuple):
            result = {}
            for key, value in key_value_tuple:
                if key.startswith("__"):
                    continue
                if isinstance(value, common.datatypes.Int):
                    result[key] = int(value)
                elif isinstance(value, common.datatypes.String):
                    result[key] = str(value)
                elif isinstance(value, common.datatypes.Bytes):
                    result[key] = bytes(value)
                elif isinstance(value, common.datatypes.Float):
                    result[key] = float(value)
                else:
                    result[key] = value
            return result

        return dataclasses.asdict(self, dict_factory=custom_data_types_dict_factory)

    def __init_subclass__(cls, **kwargs):
        _DATACLASS_MAP[cls.__name__.lower()] = cls
