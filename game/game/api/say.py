import game.constants
import game.states
from common.api_handlers import l2_request_handler
from common.ctype import ctype
from common.misc import decode_str
from common.template import Parameter, Template


@l2_request_handler(
    game.constants.GAME_REQUEST_SAY2,
    Template(
        [
            Parameter(
                id="text",
                start=0,
                type=str,
                func=decode_str(),
            ),
            Parameter(id="type", start="$text.stop", length=4, type=ctype.int32),
        ]
    ),
)
async def say2(request):
    await request.session.character.say(
        request.validated_data["type"], request.validated_data["text"]
    )
