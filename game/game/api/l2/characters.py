import game.constants
import game.packets
import game.states
from common.api_handlers import l2_request_handler
from common.datatypes import Int32, String
from common.template import Parameter, Template
from data.models.character import Character
from data.models.structures import CharacterTemplate
from game import clients


@l2_request_handler(
    game.constants.GAME_REQUEST_CHARACTER_CREATE,
    Template(
        [
            Parameter("nickname", start=0, type=String, func=String.read),
            Parameter("race", start="$nickname.stop", length=4, type=Int32),
            Parameter("sex", start="$race.stop", length=4, type=Int32),
            Parameter("class_id", start="$sex.stop", length=4, type=Int32),
            Parameter("INT", start="$class_id.stop", length=4, type=Int32),
            Parameter("STR", start="$INT.stop", length=4, type=Int32),
            Parameter("CON", start="$STR.stop", length=4, type=Int32),
            Parameter("MEN", start="$CON.stop", length=4, type=Int32),
            Parameter("DEX", start="$MEN.stop", length=4, type=Int32),
            Parameter("WIT", start="$DEX.stop", length=4, type=Int32),
            Parameter("hair_id", start="$WIT.stop", length=4, type=Int32),
            Parameter("hair_color", start="$hair_id.stop", length=4, type=Int32),
            Parameter("face_id", start="$hair_color.stop", length=4, type=Int32),
        ]
    ),
    states=[game.states.CreatingCharacter],
)
async def character_create(request):

    templates = {
        template.class_id: template
        for template in await game.clients.DATA_CLIENT.get_static(CharacterTemplate)
    }
    class_template = templates[request.validated_data["class_id"]]
    account = request.session.get_data()["account"]

    # new_char = Character(
    #     Int32.random(),
    #     account.primary_key,
    #     request.validated_data["nickname"],
    #     request.validated_data["sex"],
    #     request.validated_data["race"],
    #     request.validated_data["class_id"],
    #     100,
    #     100,
    #     100,
    #     100,
    #     100,
    #     100,
    #     face_id=request.validated_data["face_id"],
    #     hair_id=request.validated_data["hair_id"],
    #     hair_color=request.validated_data["hair_color"],
    # )

    result = None

    if result:
        request.session.set_state(game.states.WaitingCharacterSelect)
        return game.packets.CharCreateOk()
    else:
        request.session.set_state(game.states.CreatingCharacter)
        return game.packets.CharCreateFail(1)


@l2_request_handler(
    game.constants.GAME_REQUEST_NEW_CHARACTER,
    Template([]),
    states=[game.states.WaitingCharacterSelect, game.states.CreatingCharacter],
)
async def new_character(request):
    templates = await game.clients.DATA_CLIENT.get_static(CharacterTemplate)
    request.session.set_state(game.states.CreatingCharacter)
    return game.packets.CharTemplates(templates)
