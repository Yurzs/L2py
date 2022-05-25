import logging

import game.constants
import game.packets
import game.states
from common.api_handlers import l2_request_handler
from common.ctype import ctype
from common.response import Response
from common.template import Parameter, Template
from game.models.world import WORLD

LOG = logging.getLogger(f"l2py.{__name__}")


@l2_request_handler(
    game.constants.GAME_REQUEST_ACTION,
    Template(
        [
            Parameter(id="object_id", start=0, length=4, type=ctype.int32),
            Parameter(id="orig_x", start=4, length=4, type=ctype.int32),
            Parameter(id="orig_y", start=8, length=4, type=ctype.int32),
            Parameter(id="orig_z", start=12, length=4, type=ctype.int32),
            Parameter(id="shift_flag", start=16, length=1, type=ctype.int8),
        ]
    ),
)
async def action(request):
    character = request.session.character
    object_id = request.validated_data["object_id"]

    obj = WORLD.find_object_by_id(object_id)
    if obj is None:
        return game.packets.ActionFailed()

    await character.set_target(obj)
    request.session.send_packet(game.packets.MyTargetSelected(object_id=object_id, color=0))

    return

    match request.validated_data["action_id"]:
        case game.constants.ACTION_TARGET:
            if character.target != object_id:
                character.set_target(obj)
                request.session.send_packet(game.packets.MyTargetSelected(object_id, 0))
                WORLD.broadcast_target_select(character, obj)
        case game.constants.ACTION_TARGET_SHIFT:
            pass
        case _:
            LOG.info("%s is probably cheating", character.name)
            return game.packets.ActionFailed()


@l2_request_handler(
    game.constants.GAME_REQUEST_TARGET_CANCEL,
    Template([Parameter(id="unselect", start=0, length=2, type=ctype.int16)]),
)
async def target_cancel(request):
    await request.session.character.unset_target()
    request.session.send_packet(
        game.packets.TargetUnselected(
            target_id=request.session.character.id, position=request.session.character.position
        )
    )

    # WORLD.broadcast_target_unselect(request.session.character)


@l2_request_handler(
    game.constants.GAME_REQUEST_ACTION_USE,
    Template(
        [
            Parameter(id="action_id", start=0, length=4, type=ctype.int32),
            Parameter(id="with_ctrl", start=4, length=4, type=ctype.int32),
            Parameter(id="with_shift", start=8, length=1, type=ctype.int8),
        ]
    ),
)
async def action_use(request):
    action = request.validated_data["action_id"]
    character = request.session.character

    match action:
        case game.constants.ACTION_RUN:
            character.status.is_running = not character.status.is_running
            WORLD._broadcast(
                character,
                game.packets.ChangeMoveType(
                    character_id=character.id, move_type=ctype.int32(character.status.is_running)
                ),
            )
        case game.constants.ACTION_SIT:
            character.status.is_sitting = not character.status.is_sitting
            packet = game.packets.ChangeWaitType(
                character_id=character.id,
                move_type=not character.status.is_sitting,
                position=character.position,
            )
            WORLD._broadcast(character, packet)
        case game.constants.ACTION_FAKE_DEATH_START:
            pass
        case game.constants.ACTION_FAKE_DEATH_STOP:
            pass
        case game.constants.ACTION_COMMON_CRAFT:
            pass


@l2_request_handler(
    game.constants.GAME_REQUEST_SOCIAL_ACTION,
    Template(
        [
            Parameter(id="action_id", start=0, length=4, type=ctype.int32),
        ]
    ),
)
async def social_action(request):
    await request.session.character.use_social_action(request.validated_data["action_id"])
