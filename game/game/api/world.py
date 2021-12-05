from common.api_handlers import l2_request_handler
from common.template import Parameter, Template

import game.constants
import game.packets
import game.states
from game.models.world import WORLD


@l2_request_handler(
    game.constants.GAME_REQUEST_ENTER_WORLD, Template([]), states=[game.states.CharacterSelected]
)
async def enter_world(request):
    character = request.session.character

    request.session.send_packet(game.packets.EtcStatusUpdate(character))

    request.session.send_packet(game.packets.ExStorageMaxCount(character))

    request.session.send_packet(game.packets.UserInfo(character))
    WORLD.notify_spawn(character)
    WORLD.notify_me_about_others_nearby(request.session, character)

    request.session.send_packet(game.packets.ItemList(character.inventory.items))
