import src.game.game.constants
import src.game.game.states
from src.common.common.api_handlers import l2_request_handler
from src.common.common.ctype import ctype
from src.common.common.misc import decode_str
from src.common.common.template import Parameter, Template


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
