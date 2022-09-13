import game.constants
import game.packets
import game.states
from common.api_handlers import l2_request_handler
from common.template import Template
from game.models.world import WORLD
from game.request import GameRequest
from game.session import GameSession


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
    character.notify_shortcuts(request.session)

    await get_friends_list(request.session)


# TODO notify friends on Character logout
async def get_friends_list(session: GameSession):
    character = session.character
    online_friends = await character.notify_friends(session)
    if online_friends is None:
        return

    for friend in online_friends:
        friend_session = WORLD.get_session_by_character_name(friend.name)
        await friend.notify_friends(friend_session)
