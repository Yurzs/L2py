import logging

import game.clients
import game.constants
import game.packets
from common.api_handlers import l2_request_handler
from common.template import Parameter, Template
from data.models.character import Character
from game.states import Connected, WaitingAuthentication

LOG = logging.getLogger(f"l2py.{__name__}")


@l2_request_handler(
    game.constants.GAME_REQUEST_PROTOCOL_VERSION,
    Template([Parameter("protocol_version", start=0, length=4, type=Int32)]),
    states=[Connected],
)
async def protocol_version(request):

    if (
        request.validated_data["protocol_version"] != 746
        and request.validated_data["protocol_version"] != 251
    ):
        return game.packets.CryptInit(False, request.session.xor_key.outgoing_key)

    elif request.validated_data["protocol_version"] == -1:
        return game.packets.CryptInit(False, request.session.xor_key.outgoing_key)

    else:
        request.session.set_state(WaitingAuthentication)
        request.session.send_packet(
            game.packets.CryptInit(True, request.session.xor_key.outgoing_key)
        )
        request.session.encryption_enabled = True


@l2_request_handler(
    game.constants.GAME_REQUEST_AUTH_LOGIN,
    Template(
        [
            Parameter("login", start=0, type=String, func=String.read),
            Parameter("play_ok2", start="$login.stop", length=4, type=Int32),
            Parameter("play_ok1", start="$play_ok2.stop", length=4, type=Int32),
            Parameter("login_ok1", start="$play_ok1.stop", length=4, type=Int32),
            Parameter("login_ok2", start="$login_ok1.stop", length=4, type=Int32),
        ]
    ),
    states=[WaitingAuthentication],
)
async def auth_login(request):

    auth_result = await game.clients.LOGIN_CLIENT.auth_login(
        request.validated_data["login"],
        request.validated_data["login_ok1"],
        request.validated_data["login_ok2"],
        request.validated_data["play_ok1"],
        request.validated_data["play_ok2"],
    )

    if auth_result["authenticated"]:
        account = auth_result["account"]
        request.session.set_data({"account": account})
        request.session.set_state(game.states.WaitingCharacterSelect)
        return game.packets.CharList(await Character.all(account_username=account.username))

    return game.packets.AuthLoginFail(game.constants.GAME_AUTH_LOGIN_FAIL_DEFAULT)
