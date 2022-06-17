import src.game.game.constants
import src.game.game.packets
import src.game.game.states
from src.common.common.api_handlers import l2_request_handler
from src.common.common.template import Parameter, Template
from src.game.game.models.world import WORLD
from src.game.game.request import GameRequest


@l2_request_handler(
    game.constants.GAME_REQUEST_ENTER_WORLD,
    Template([]),
    states=[game.states.CharacterSelected],
)
async def enter_world(request: GameRequest):
    character = request.session.character

    request.session.send_packet(game.packets.EtcStatusUpdate(character=character))

    request.session.send_packet(game.packets.ExStorageMaxCount(character=character))

    request.session.send_packet(game.packets.UserInfo(character=character))
    await character.spawn()
    WORLD.notify_me_about_others_nearby(request.session, character)

    request.session.send_packet(game.packets.ItemList(items=character.inventory.items))

    character.notify_macros(request.session)
