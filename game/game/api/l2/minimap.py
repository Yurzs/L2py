import game.constants
import game.packets
import game.states
from common.api_handlers import l2_request_handler
from common.template import Parameter, Template
from data.models.character import Character
from data.models.structures.object.point3d import Point3D
from data.models.structures.object.position import Position
from game.models.world import WORLD


@l2_request_handler(game.constants.GAME_REQUEST_OPEN_MINIMAP, Template([]))
async def open_minimap(request):
    return game.packets.OpenMinimap(1665, game.constants.SEVEN_SIGNS_PERIOD_COMPETITION_RECRUITING)
