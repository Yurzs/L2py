from common.api_handlers import l2_request_handler
import game.constants
from common.template import Template, Parameter
from common.datatypes import String, Int32


@l2_request_handler(
    game.constants.GAME_REQUEST_CHARACTER_CREATE,
    Template([
        Parameter("nickname", start=0, type=String, func=String.decode),
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
    ]),
)
async def character_create(request):
    print(request.validated_data)
