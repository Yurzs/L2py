import game.constants
import game.states
from common.api_handlers import l2_request_handler
from common.ctype import ctype
from common.misc import decode_str
from common.template import Parameter, Template


@l2_request_handler(
    game.constants.GAME_REQUEST_JOIN_PARTY,
    Template(
        [
            Parameter(
                id="name",
                start=0,
                type=str,
                func=decode_str(),
            ),
            Parameter(
                id="item_distribution", start="$text.stop", length=4, type=ctype.int32
            ),
        ]
    ),
)
async def join_party(request):
    pass
