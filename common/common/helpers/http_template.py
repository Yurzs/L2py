import dataclasses

from common.dataclass import BaseDataclass


def template_from_dataclass(dataclass):

    template = {}
    for field_name, field in dataclass.__annotations__.items():
        if not field_name.startswith("__"):
            if issubclass(field, BaseDataclass):
                template[field_name] = template_from_dataclass(field)
            else:
                template[field_name] = field

    template["$model"] = str
    template["__required__"] = []

    for field_name, field in dataclass.__dataclass_fields__.items():
        if field_name in template:
            if isinstance(field.default, dataclasses._MISSING_TYPE):
                template["__required__"].append(field_name)
    return template
