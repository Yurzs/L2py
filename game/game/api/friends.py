import logging

from common.api_handlers import l2_request_handler
from common.ctype import ctype
from common.misc import decode_str
from common.template import Parameter, Template
from game.constants import (
    GAME_REQUEST_FRIEND_DELETE,
    GAME_REQUEST_FRIEND_INVITE,
    GAME_REQUEST_FRIEND_INVITE_ANSWER,
    GAME_REQUEST_FRIEND_MESSAGE,
)
from game.models.world import WORLD
from game.packets import FriendInvite, FriendMessage
from game.request import GameRequest

LOG = logging.getLogger(f"l2py.{__name__}")


@l2_request_handler(
    GAME_REQUEST_FRIEND_INVITE,
    Template([Parameter(id="friend_name", start=0, type=str, func=decode_str())]),
)
async def friend_invite(request: GameRequest):
    friend_name = request.validated_data["friend_name"]
    if friend_name is None:
        return

    requestor_name = request.session.character.name
    requestor_friends = request.session.character.friends

    friend_session = WORLD.get_session_by_character_name(friend_name)
    if friend_session is None:
        LOG.debug(
            f"{requestor_name} has tried to invite to friends offline (not existing) player: {friend_name}"
        )
        # TODO: SysMsg: THE_USER_YOU_REQUESTED_IS_NOT_IN_GAME

    elif requestor_name == friend_name:
        LOG.debug(f"{requestor_name} has tried to invite to friends himself")
        # TODO: SysMsg: YOU_CANNOT_ADD_YOURSELF_TO_OWN_FRIEND_LIST

    elif friend_session.character.id in requestor_friends:
        LOG.debug(f"{requestor_name} has tried to invite to friends his friend: {friend_name}")
        # TODO: SysMsg: S1_ALREADY_IN_FRIENDS_LIST

    else:
        requestor_id = request.session.character.id

        friend_session.character.active_requestor = requestor_id  # to be discussed
        friend_session.send_packet(FriendInvite(requestor_name=requestor_name))

        # TODO SysMsg: S1_IS_BUSY_TRY_LATER

        LOG.info(f"{requestor_name} has invited to friends player: {friend_name}")
        # TODO SysMsg: S1_REQUESTED_TO_BECOME_FRIENDS


@l2_request_handler(
    GAME_REQUEST_FRIEND_INVITE_ANSWER,
    Template([Parameter(id="answer_type", start=0, length=4, type=ctype.int32)]),
)
async def friend_invite_answer(request: GameRequest):
    friend_character = request.session.character
    requestor_id = friend_character.active_requestor
    requstor_character = WORLD.get_character_by_id(requestor_id)
    requstor_session = requstor_character.session

    answer_type = request.validated_data["answer_type"]
    if answer_type == 1:
        friend_character.friends.append(requestor_id)
        requstor_character.friends.append(friend_character.id)

        friend_character.active_requestor = 0  # to be discussed

        await friend_character.commit_changes(fields=["friends"])
        await requstor_character.commit_changes(fields=["friends"])

        await friend_character.notify_friends(request.session)
        # TODO: SysMsg: S1_JOINED_AS_FRIEND
        await requstor_character.notify_friends(requstor_session)
        # TODO: SysMsg: S1_ADDED_TO_FRIENDS

        LOG.info(
            f"{friend_character.name} has accepted friend invite from {requstor_character.name}"
        )

    else:
        LOG.info(
            f"{friend_character.name} failed to accept friend invite from {requstor_character.name}"
        )
        # TODO SysMsg: FAILED_TO_INVITE_A_FRIEND


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
    if recipient_session is None:
        LOG.debug(
            f"{name} has tried to send friend message {message} to the offline player: {recipient_name}"
        )
        # TODO: SysMsg: TARGET_IS_NOT_FOUND_IN_THE_GAME
        return

    recipient_session.send_packet(
        FriendMessage(sender_name=name, message=message, recipient_name=recipient_name)
    )
    LOG.info(f'{name} has send friend message: "{message}" to {recipient_name}')


@l2_request_handler(
    GAME_REQUEST_FRIEND_DELETE,
    Template([Parameter(id="friend_name", start=0, type=str, func=decode_str())]),
)
async def friend_delete(request: GameRequest):
    friend_to_delete_name = request.validated_data["friend_name"]
    if friend_to_delete_name is None:
        return

    character = request.session.character
    friend_character = await character.one_by_name(friend_to_delete_name, required=False)
    if friend_character is None:
        LOG.debug(f"{character.name} tried to delete not existing player {friend_to_delete_name}")
        return

    if friend_character.id not in character.friends:
        LOG.debug(f"{character.name} tried to delete not his friend {friend_to_delete_name}")
        # TODO: SysMsg: S1_NOT_ON_YOUR_FRIENDS_LIST
        return

    character.friends.remove(friend_character.id)
    friend_character.friends.remove(character.id)

    await character.commit_changes(fields=["friends"])
    await friend_character.commit_changes(fields=["friends"])
    LOG.info(f"{character.name} has deleted his friend {friend_to_delete_name}")

    await character.notify_friends(request.session)

    friend_session = WORLD.get_session_by_character_name(friend_to_delete_name)
    if friend_session is not None:
        await friend_character.notify_friends(friend_session)

    # TODO: SysMsg: S1_HAS_BEEN_DELETED_FROM_YOUR_FRIENDS_LIST
