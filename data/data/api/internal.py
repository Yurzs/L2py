from aiojsonapi import JsonTemplate, routes

from common.document import _ADAPTER


@routes.post("/api/data/internal/model.query")
@JsonTemplate(
    {
        "database": str,
        "collection": str,
        "action": str,
        "args": list,
        "kwargs": dict,
        "__required__": ["__all__"],
    }
)
async def model_query(request, validated_data):
    # TODO: SECURITY HAZARD

    return await _ADAPTER["adapter"].proceed_action(validated_data)
