import logging

import game.constants
import game.packets
from common.api_handlers import l2_request_handler
from common.ctype import ctype
from common.misc import decode_str
from common.models import Account
from common.template import Parameter, Template
from game.models.character import Character
from game.states import Connected, WaitingAuthentication

LOG = logging.getLogger(f"l2py.{__name__}")


@l2_request_handler(
    game.constants.GAME_REQUEST_PROTOCOL_VERSION,
    Template([Parameter(id="protocol_version", start=0, length=4, type=ctype.int)]),
    states=[Connected],
)
async def protocol_version(request):

    if (
        request.validated_data["protocol_version"] != 746
        and request.validated_data["protocol_version"] != 251
    ):
        return game.packets.CryptInit(is_valid=False, xor_key=request.session.xor_key.outgoing_key)

    elif request.validated_data["protocol_version"] == -1:
        return game.packets.CryptInit(is_valid=False, xor_key=request.session.xor_key.outgoing_key)

    else:
        request.session.set_state(WaitingAuthentication)
        request.session.send_packet(
            game.packets.CryptInit(is_valid=True, xor_key=request.session.xor_key.outgoing_key)
        )
        request.session.encryption_enabled = True


@l2_request_handler(
    game.constants.GAME_REQUEST_AUTH_LOGIN,
    Template(
        [
            Parameter(id="login", start=0, type=str, func=decode_str()),
            Parameter(id="play_ok2", start="$login.stop", length=4, type=ctype.int),
            Parameter(id="play_ok1", start="$play_ok2.stop", length=4, type=ctype.int),
            Parameter(id="login_ok1", start="$play_ok1.stop", length=4, type=ctype.int),
            Parameter(id="login_ok2", start="$login_ok1.stop", length=4, type=ctype.int),
        ]
    ),
    states=[WaitingAuthentication],
)
async def auth_login(request):

    account = await Account.one(username=request.validated_data["login"], required=False)
    if account is not None:
        if (
            account.game_auth.login_ok1 == request.validated_data["login_ok1"]
            and account.game_auth.login_ok2 == request.validated_data["login_ok2"]
            and account.game_auth.play_ok1 == request.validated_data["play_ok1"]
            and account.game_auth.play_ok2 == request.validated_data["play_ok2"]
        ):
            request.session.account = account
            request.session.set_state(game.states.WaitingCharacterSelect)
            return game.packets.CharList(
                characters=await Character.all(account_username=account.username)
            )

        return game.packets.AuthLoginFail(
            reason_id=game.constants.GAME_AUTH_LOGIN_FAIL_PASSWORD_DOESNT_MATCH
        )
    return game.packets.AuthLoginFail(reason_id=game.constants.GAME_AUTH_LOGIN_FAIL_DEFAULT)
