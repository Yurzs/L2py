import game.constants
import game.packets
import game.states
from common.api_handlers import l2_request_handler
from common.template import Template


@l2_request_handler(game.constants.GAME_REQUEST_OPEN_MINIMAP, Template([]))
async def open_minimap(request):
    return game.packets.OpenMinimap(
        map_id=1665,
        seven_signs_period=game.constants.SEVEN_SIGNS_PERIOD_COMPETITION_RECRUITING,
    )
