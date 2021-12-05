from common.api_handlers import l2_request_handler
from common.template import Parameter, Template

import game.constants
import game.packets
import game.states
from game.models.character import Character
from game.models.structures.object.point3d import Point3D
from game.models.structures.object.position import Position
from game.models.world import WORLD


@l2_request_handler(
    game.constants.GAME_REQUEST_MOVE_BACK_TO_LOCATION,
    Template(
        [
            Parameter("to_x", start=0, length=4, type=Int32),
            Parameter("to_y", start="$to_x.stop", length=4, type=Int32),
            Parameter("to_z", start="$to_y.stop", length=4, type=Int32),
            Parameter("from_x", start="$to_z.stop", length=4, type=Int32),
            Parameter("from_y", start="$from_x.stop", length=4, type=Int32),
            Parameter("from_z", start="$from_y.stop", length=4, type=Int32),
            Parameter("by_mouse", start="$from_z.stop", length=4, type=Bool),
        ]
    ),
    states="*",  # TODO
)
async def move_back_to_location(request):
    character: Character = request.session.character

    if not request.validated_data["by_mouse"]:
        return game.packets.ActionFailed()
    # TODO check for attack

    to_x = request.validated_data["to_x"]
    to_y = request.validated_data["to_y"]
    to_z = request.validated_data["to_z"]

    diff_x = Double(to_x - character.position.point3d.x)
    diff_y = Double(to_y - character.position.point3d.y)

    print(diff_x, diff_y)
    if (diff_x * diff_x + diff_y * diff_y) > 98010000:
        return game.packets.ActionFailed()

    new_position = Position(
        0,
        Point3D(
            to_x,
            to_y,
            to_z,
        ),
    )
    character.position.point3d.z = request.validated_data["from_z"]

    request.session.send_packet(game.packets.CharMoveToLocation(character, new_position))
    WORLD.notify_move(character, new_position)
    character.position = new_position


@l2_request_handler(
    game.constants.GAME_REQUEST_VALIDATE_POSITION,
    Template(
        [
            Parameter("x", start=0, length=4, type=Int32),
            Parameter("y", start="$x.stop", length=4, type=Int32),
            Parameter("z", start="$y.stop", length=4, type=Int32),
            Parameter("heading", start="$z.stop", length=4, type=Int32),
            Parameter("data", start="$heading.stop", length=4, type=Int32),
        ]
    ),
    states="*",  # TODO
)
async def validate_position(request):
    pass
