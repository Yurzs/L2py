import src.game.game.constants
import src.game.game.packets
import src.game.game.states
import src.game.game as game
from src.common.common.api_handlers import l2_request_handler
from src.common.common.ctype import ctype
from src.common.common.response import Response
from src.common.common.template import Parameter, Template
from src.game.game.models.world import WORLD


@l2_request_handler(
    game.constants.GAME_REQUEST_ATTACK,
    Template(
        [
            Parameter(id="object_id", start=0, length=4, type=ctype.int),
            Parameter(id="shift_flag", start=16, length=1, type=ctype.bool),
        ]
    ),
)
async def attack(request):
    character = request.session.character
    attack_packet = game.packets.Attack(
        character.id,
        False,
        ctype.int32(0),
        character.position,
        game.packets.Attack.Hit(target_id=request.validated_data["object_id"], damage=1),
    )
    request.session.send_packet(attack_packet)
    WORLD.broadcast_attack(character, attack_packet)
