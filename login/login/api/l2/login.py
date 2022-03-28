import logging

import login.constants
from common.api_handlers import l2_request_handler
from common.client.exceptions import ApiException, WrongCredentials
from common.helpers.cython import cython, utf8str
from common.models import Account, GameServer
from common.template import Parameter, Template
from login.api.l2.handlers import verify_secrets
from login.packets import GGAuth, LoginFail, LoginOk, PlayFail, PlayOk, ServerList
from login.state import Authenticated, Connected, GGAuthenticated, WaitingGameServerSelect

LOG = logging.getLogger(f"l2py.{__name__}")


@l2_request_handler(
    login.constants.REQUEST_AUTH_LOGIN,
    Template(
        [],
    ),
    states=[GGAuthenticated],
)
async def auth_login(request):

    encrypted = bytearray(request.data[0:128])
    decrypted = request.session.rsa_key.private_decrypt(encrypted)
    try:
        username = utf8str.decode(decrypted[94:107])
        password = utf8str.decode(decrypted[108:124])
    except UnicodeDecodeError:
        return LoginFail(login.constants.LOGIN_FAIL_WRONG_LOGIN_OR_PASSWORD)

    try:
        account = await Account.one(username=username, required=False)
        if account is None:
            account = Account(username, username, "none", 1)
            await account.insert()
            await account.set_new_password(password)
        print(account)
        if not account.authenticate(password):
            raise WrongCredentials("Wrong Password")
    except WrongCredentials:
        return LoginFail(login.constants.LOGIN_FAIL_WRONG_LOGIN_OR_PASSWORD)
    except ApiException:
        return LoginFail(login.constants.LOGIN_FAIL_DATABASE_ERROR)
    except Exception as e:
        LOG.exception(e)
        return LoginFail(login.constants.LOGIN_FAIL_WRONG_PASSWORD)

    request.session.set_state(Authenticated)
    request.session.account = account

    return LoginOk(request.session.session_key.login_ok1, request.session.session_key.login_ok2)


@l2_request_handler(login.constants.REQUEST_GG_AUTH, Template([]), states=[Connected])
async def gg_authenticated(request):
    request.session.set_state(GGAuthenticated)
    return GGAuth()


@l2_request_handler(
    login.constants.REQUEST_SERVER_LIST,
    Template(
        [
            Parameter("login_ok1", start=0, length=4, type=cython.long),
            Parameter("login_ok2", start=4, length=4, type=cython.long),
        ]
    ),
    states=[Authenticated],
)
@verify_secrets
async def server_list(request):
    game_servers = await GameServer.all()
    request.session.set_state(WaitingGameServerSelect)
    return ServerList(game_servers)


@l2_request_handler(
    login.constants.REQUEST_SERVER_LOGIN,
    Template(
        [
            Parameter("login_ok1", start=0, length=4, type=cython.long),
            Parameter("login_ok2", start=4, length=4, type=cython.long),
            Parameter("server_id", start=8, length=1, type=cython.char),
        ]
    ),
    states=[WaitingGameServerSelect],
)
@verify_secrets
async def server_login(request):
    game_servers = await GameServer.all()
    game_server = None

    for server in game_servers:
        if server.id == request.validated_data["server_id"]:
            game_server = server
            break

    if game_server is None:
        return PlayFail(login.constants.PLAY_FAIL_ACCESS_DENIED)

    if game_server.is_full:
        return PlayFail(login.constants.PLAY_FAIL_TOO_MANY_USERS)

    request.session.send_packet(
        PlayOk(request.session.session_key.play_ok1, request.session.session_key.play_ok2)
    )
    await request.session.account.login_authenticated(
        game_server.id,
        request.session.session_key.play_ok1,
        request.session.session_key.play_ok2,
        request.session.session_key.login_ok1,
        request.session.session_key.login_ok2,
    )
