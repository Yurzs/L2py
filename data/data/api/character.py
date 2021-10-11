from aiojsonapi import JsonTemplate, routes

from common.helpers.http_template import template_from_dataclass
from data.models.character import Character


@routes.post("/api/character.create")
@JsonTemplate(
    {
        "character": Character,
        "__required__": ["character"],
    }
)
async def create(request, validated_data):

    character: Character = validated_data["character"]
    await character.insert()
    return True
