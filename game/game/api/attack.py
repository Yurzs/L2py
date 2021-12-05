from common.api_handlers import l2_request_handler
from common.response import Response
from common.template import Parameter, Template

import game.constants
import game.packets
import game.states
from game.models.world import WORLD


@l2_request_handler(
    game.constants.GAME_REQUEST_ATTACK,
    Template(
        [
            Parameter("object_id", start=0, length=4, type=Int32),
            Parameter("shift_flag", start=16, length=1, type=Bool),
        ]
    ),
)
async def attack(request):
    character = request.session.character
    attack_packet = game.packets.Attack(
        character.id,
        False,
        Int32(0),
        character.position,
        game.packets.Attack.Hit(request.validated_data["object_id"], 1),
    )
    request.session.send_packet(attack_packet)
    WORLD.broadcast_attack(character, attack_packet)
