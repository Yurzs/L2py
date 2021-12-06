import game.constants
import game.states
from common.api_handlers import l2_request_handler
from common.template import Parameter, Template
from game.models.world import WORLD


@l2_request_handler(
    game.constants.GAME_REQUEST_SAY2,
    Template(
        [
            Parameter(
                "text",
                start=0,
                type=UTFString,
                func=UTFString.read,
            ),
            Parameter("type", start="$text.stop", length=4, type=Int32),
        ]
    ),
)
async def say2(request):
    character = request.session.character
    WORLD.say(
        character,
        request.validated_data["type"],
        character.name,
        request.validated_data["text"],
        session=request.session,
    )
