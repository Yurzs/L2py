import logging

from common.api_handlers import l2_request_handler
from common.ctype import ctype
from common.misc import decode_str
from common.template import Parameter, Template
from game.api.world import get_friends_list
from game.constants import (
    GAME_REQUEST_FRIEND_INVITE,
    GAME_REQUEST_FRIEND_INVITE_ANSWER,
    GAME_REQUEST_FRIEND_MESSAGE,
)
from game.models.world import WORLD
from game.packets import FriendInvite, FriendList, FriendMessage
from game.request import GameRequest

LOG = logging.getLogger(f"l2py.{__name__}")


@l2_request_handler(
    GAME_REQUEST_FRIEND_INVITE,
    Template([Parameter(id="friend_name", start=0, type=str, func=decode_str())]),
)
async def friend_invite(request: GameRequest):
    friend_name = request.validated_data["friend_name"]

    friend_session = WORLD.get_session_by_character_name(friend_name)
    if friend_session is not None:
        requestor_id = request.session.character.id
        requestor_name = request.session.character.name

        friend_session.character.active_requestor = requestor_id  # to be discussed

        friend_session.send_packet(FriendInvite(requestor_name=requestor_name))


@l2_request_handler(
    GAME_REQUEST_FRIEND_INVITE_ANSWER,
    Template([Parameter(id="answer_type", start=0, length=4, type=ctype.int32)]),
)
async def friend_invite_answer(request: GameRequest):
    answer_type = request.validated_data["answer_type"]
    if answer_type == 1:
        LOG.info("OK")

        friend_character = request.session.character
        requestor_id = friend_character.active_requestor
        requstor_character = WORLD.get_character_by_id(requestor_id)

        friend_character.friends.append(requestor_id)
        requstor_character.friends.append(friend_character.id)
        requestor_session = WORLD.get_session_by_character(requstor_character)

        friend_character.active_requestor = 0  # to be discussed

        await friend_character.commit_changes(fields=["friends"])
        await requstor_character.commit_changes(fields=["friends"])

        await get_friends_list(request.session)
        await get_friends_list(requestor_session)

    else:
        LOG.info("NOK")


@l2_request_handler(
    GAME_REQUEST_FRIEND_MESSAGE,
    Template(
        [
            Parameter(id="message", start=0, type=str, func=decode_str()),
            Parameter(id="recipient_name", start="$message.stop", type=str, func=decode_str()),
        ]
    ),
)
async def send_friend_message(request: GameRequest):
    name = request.session.character.name
    message = request.validated_data["message"]
    recipient_name = request.validated_data["recipient_name"]

    recipient_session = WORLD.get_session_by_character_name(recipient_name)

    recipient_session.send_packet(
        FriendMessage(sender_name=name, message=message, recipient_name=recipient_name)
    )
