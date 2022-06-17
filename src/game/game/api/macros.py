import src.game.game.constants
import src.game.game.states
from src.common.common.api_handlers import l2_request_handler
from src.common.common.ctype import ctype
from src.common.common.misc import decode_str
from src.common.common.template import Parameter, Template
from src.game.game.models.structures.macro import Macro, MacroEntry
from src.game.game.request import GameRequest


@l2_request_handler(
    game.constants.GAME_REQUEST_MAKE_MACRO,
    Template(
        [
            Parameter(
                id="macro_id",
                start=0,
                length=4,
                type=ctype.int32,
            ),
            Parameter(
                id="name",
                start="$macro_id.stop",
                type=str,
                func=decode_str(),
            ),
            Parameter(
                id="description",
                start="$name.stop",
                type=str,
                func=decode_str(),
            ),
            Parameter(
                id="acronym",
                start="$description.stop",
                type=str,
                func=decode_str(),
            ),
            Parameter(
                id="icon",
                start="$acronym.stop",
                length=1,
                type=ctype.int8,
            ),
            Parameter(
                id="macro_count",
                start="$icon.stop",
                length=1,
                type=ctype.int8,
            ),
            Parameter(
                id="macros",
                start="$macro_count.stop",
                type=Template(
                    [
                        Parameter(id="entry_id", start=0, length=1, type=ctype.int8),
                        Parameter(id="type", start=1, length=1, type=ctype.int8),
                        Parameter(id="skill_id", start=2, length=4, type=ctype.int32),
                        Parameter(id="shortcut_id", start=6, length=1, type=ctype.int8),
                        Parameter(id="command", start=7, type=str, func=decode_str()),
                    ],
                ),
                repeat="$macro_count",
            ),
        ]
    ),
)
async def create_macro(request: GameRequest):

    character = request.session.character

    macro_id = 0

    if request.validated_data["macro_id"] != 0:  # modification of existing
        macros = {macro.id: macro for macro in character.macros}
        macro_to_delete = macros[request.validated_data["macro_id"]]
        character.macros.remove(macro_to_delete)
        macro_id = macro_to_delete.id

    if macro_id == 0:
        macro_id = 1
        existing_ids = [macro.id for macro in character.macros]
        for _ in range(9999):
            if macro_id in existing_ids:
                macro_id += 1
            else:
                break

    macro = Macro(
        id=macro_id,
        name=request.validated_data["name"],
        acronym=request.validated_data["acronym"],
        description=request.validated_data["description"],
        entries=[MacroEntry(**macro) for macro in request.validated_data["macros"]],
        icon=request.validated_data["icon"],
    )
    character.macros.append(macro)

    character.macros_revision += 1
    await character.commit_changes(fields=["macros"])

    character.notify_macros(request.session)


@l2_request_handler(
    game.constants.GAME_REQUEST_DELETE_MACRO,
    Template(
        [
            Parameter(
                id="macro_id",
                start=0,
                length=4,
                type=ctype.int32,
            ),
        ]
    ),
)
async def delete_macro(request):

    character = request.session.character

    for macro in character.macros.copy():
        if macro.id == request.validated_data["macro_id"]:
            character.macros.remove(macro)

    await character.commit_changes(fields=["macros"])

    character.macros_revision += 1
    character.notify_macros(request.session)
