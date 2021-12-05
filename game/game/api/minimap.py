from common.api_handlers import l2_request_handler
from common.template import Template

import game.constants
import game.packets
import game.states


@l2_request_handler(game.constants.GAME_REQUEST_OPEN_MINIMAP, Template([]))
async def open_minimap(request):
    return game.packets.OpenMinimap(1665, game.constants.SEVEN_SIGNS_PERIOD_COMPETITION_RECRUITING)
