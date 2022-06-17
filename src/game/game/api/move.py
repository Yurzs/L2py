import src.game.game.constants
import src.game.game.packets
import src.game.game.states
from src.common.common.api_handlers import l2_request_handler
from src.common.common.ctype import ctype
from src.common.common.template import Parameter, Template
from src.game.game.models.character import Character
from src.game.game.models.structures.object.point3d import Point3D
from src.game.game.models.structures.object.position import Position


@l2_request_handler(
    game.constants.GAME_REQUEST_MOVE_BACK_TO_LOCATION,
    Template(
        [
            Parameter(id="to_x", start=0, length=4, type=ctype.int32),
            Parameter(id="to_y", start="$to_x.stop", length=4, type=ctype.int32),
            Parameter(id="to_z", start="$to_y.stop", length=4, type=ctype.int32),
            Parameter(id="from_x", start="$to_z.stop", length=4, type=ctype.int32),
            Parameter(id="from_y", start="$from_x.stop", length=4, type=ctype.int32),
            Parameter(id="from_z", start="$from_y.stop", length=4, type=ctype.int32),
            Parameter(id="by_mouse", start="$from_z.stop", length=4, type=ctype.int32),
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

    diff_x: ctype.double = to_x - character.position.point3d.x
    diff_y: ctype.double = to_y - character.position.point3d.y

    if (diff_x * diff_x + diff_y * diff_y) > 98010000:
        return game.packets.ActionFailed()

    new_position = Position(
        heading_angle=0,
        point3d=Point3D(
            x=to_x,
            y=to_y,
            z=to_z,
        ),
    )

    await character.move(new_position)
    await character.commit_changes(fields=["position"])


@l2_request_handler(
    game.constants.GAME_REQUEST_VALIDATE_POSITION,
    Template(
        [
            Parameter(id="x", start=0, length=4, type=ctype.int32),
            Parameter(id="y", start="$x.stop", length=4, type=ctype.int32),
            Parameter(id="z", start="$y.stop", length=4, type=ctype.int32),
            Parameter(id="heading", start="$z.stop", length=4, type=ctype.int32),
            Parameter(id="data", start="$heading.stop", length=4, type=ctype.int32),
        ]
    ),
    states="*",  # TODO
)
async def validate_position(request):
    pass
