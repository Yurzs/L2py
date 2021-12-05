import logging

from common.api_handlers import l2_request_handler
from common.response import Response
from common.template import Parameter, Template

import game.constants
import game.packets
import game.states
from game.models.world import WORLD

LOG = logging.getLogger(f"l2py.{__name__}")


@l2_request_handler(
    game.constants.GAME_REQUEST_ACTION,
    Template(
        [
            Parameter("object_id", start=0, length=4, type=Int32),
            Parameter("action_id", start=16, length=4, type=Int32),
        ]
    ),
)
async def action(request):
    character = request.session.character
    object_id = request.validated_data["object_id"]

    obj = WORLD.find_object_by_id(object_id)
    if obj is None:
        return game.packets.ActionFailed()

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
    Template([Parameter("unselect", start=0, length=2, type=Int16)]),
)
async def target_cancel(request):
    request.session.character.set_target(None)
    request.session.send_packet(
        game.packets.TargetUnselected(
            request.session.character.id, request.session.character.position
        )
    )
    WORLD.broadcast_target_unselect(request.session.character)


@l2_request_handler(
    game.constants.GAME_REQUEST_ACTION_USE,
    Template(
        [
            Parameter("action_id", start=0, length=4, type=Int32),
            Parameter("with_ctrl", start=4, length=4, type=Int32),
            Parameter("with_shift", start=8, length=4, type=Int32),
        ]
    ),
)
async def action_use(request):
    action = request.validated_data["action_id"]
    character = request.session.character

    match action:
        case game.constants.ACTION_RUN:
            character.status.is_running = not character.status.is_running
            WORLD.broadcast(
                character,
                game.packets.ChangeMoveType(character.id, character.status.is_running),
            )
        case game.constants.ACTION_SIT:
            character.status.is_sitting = not character.status.is_sitting
            packet = game.packets.ChangeWaitType(
                character.id, Bool(not character.status.is_sitting), character.position
            )
            WORLD.broadcast(character, packet)
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
            Parameter("action_id", start=0, length=4, type=Int32),
        ]
    ),
)
async def social_action(request):
    action_id = request.validated_data["action_id"]
    character = request.session.character

    if action_id in game.constants.PUBLIC_SOCIAL_ACTIONS:
        WORLD.broadcast(
            request.session.character,
            game.packets.SocialAction(
                character.id,
                action_id,
            ),
        )
