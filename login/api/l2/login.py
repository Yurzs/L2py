import logging

from M2Crypto import RSA

import login.constants
from common.api_handlers import l2_request_handler
from common.client.exceptions import ApiException, WrongCredentials
from common.datatypes import Int8, String
from common.helpers.bytearray import ByteArray
from common.template import Parameter, Template
from login.api.l2.handlers import verify_secrets
from login.clients import data_client
from login.packets import GGAuth, LoginFail, LoginOk, PlayFail, PlayOk, ServerList
from login.state import (
    Authenticated,
    Connected,
    GGAuthenticated,
    WaitingGameServerSelect,
)

LOG = logging.getLogger(f"l2py.{__name__}")


@l2_request_handler(
    login.constants.REQUEST_AUTH_LOGIN,
    Template(
        [],
    ),
    states=[GGAuthenticated],
)
async def auth_login(request):

    encrypted = ByteArray(request.data[0:128])
    key = request.session.rsa_key.m2crypto_key
    decrypted = key.private_decrypt(bytes(encrypted), RSA.no_padding)
    try:
        username = String.decode(decrypted[94:107])
        password = String.decode(decrypted[108:124])
    except UnicodeDecodeError:
        return LoginFail(login.constants.LOGIN_FAIL_WRONG_LOGIN_OR_PASSWORD)

    try:
        response = await data_client.authenticate(username, password)
        if not response["authenticated"]:
            raise WrongCredentials("Wrong Password")
        account = response["account"]
    except WrongCredentials:
        return LoginFail(login.constants.LOGIN_FAIL_WRONG_LOGIN_OR_PASSWORD)
    except ApiException:
        return LoginFail(login.constants.LOGIN_FAIL_DATABASE_ERROR)
    except Exception as e:
        LOG.exception(e)
        return LoginFail(login.constants.LOGIN_FAIL_WRONG_PASSWORD)

    request.session.set_state(Authenticated)
    request.session.set_data({"account": account})

    return LoginOk(
        request.session.session_key.login_ok1, request.session.session_key.login_ok2
    )


@l2_request_handler(login.constants.REQUEST_GG_AUTH, Template([]), states=[Connected])
async def gg_authenticated(request):
    request.session.set_state(GGAuthenticated)
    return GGAuth()


@l2_request_handler(
    login.constants.REQUEST_SERVER_LIST,
    Template(
        [
            Parameter("login_ok1", start=0, length=4, type=ByteArray),
            Parameter("login_ok2", start=4, length=4, type=ByteArray),
        ]
    ),
    states=[Authenticated],
)
@verify_secrets
async def server_list(request):
    game_servers = await data_client.get_game_server_list()
    request.session.set_state(WaitingGameServerSelect)
    request.session.set_data(
        {
            "login_ok1": request.session.session_key.login_ok1,
            "login_ok2": request.session.session_key.login_ok2,
            "play_ok1": request.session.session_key.play_ok1,
            "play_ok2": request.session.session_key.play_ok2,
        }
    )
    return ServerList(game_servers)


@l2_request_handler(
    login.constants.REQUEST_SERVER_LOGIN,
    Template(
        [
            Parameter("login_ok1", start=0, length=4, type=ByteArray),
            Parameter("login_ok2", start=4, length=4, type=ByteArray),
            Parameter("server_id", start=8, length=1, type=Int8),
        ]
    ),
    states=[WaitingGameServerSelect],
)
@verify_secrets
async def server_login(request):
    game_servers = await data_client.get_game_server_list()
    game_server = None

    for server in game_servers:
        if server.id == request.validated_data["server_id"]:
            game_server = server
            break

    if game_server is None:
        return PlayFail(login.constants.PLAY_FAIL_ACCESS_DENIED)

    if game_server.is_full:
        return PlayFail(login.constants.PLAY_FAIL_TOO_MANY_USERS)

    return PlayOk(
        request.session.session_key.play_ok1, request.session.session_key.play_ok2
    )
