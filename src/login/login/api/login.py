import logging

import login.constants
from src.common.common.api_handlers import l2_request_handler
from src.common.common.client.exceptions import ApiException, WrongCredentials
from src.common.common.ctype import ctype
from src.common.common.misc import decode_str
from src.common.common.models import Account, GameServer
from src.common.common.template import Parameter, Template
from src.login.login.api.handlers import verify_secrets
from src.login.login.packets import GGAuth, LoginFail, LoginOk, PlayFail, PlayOk, ServerList
from src.login.login.state import Authenticated, Connected, GGAuthenticated, WaitingGameServerSelect

LOG = logging.getLogger(f"l2py.{__name__}")


@l2_request_handler(
    login.constants.REQUEST_AUTH_LOGIN,
    Template([]),
    states=[GGAuthenticated],
)
async def auth_login(request):

    encrypted = bytearray(request.data[0:128])
    decrypted = request.session.rsa_key.private_decrypt(encrypted)
    try:
        username = decode_str("utf-8")(decrypted[94:107])[0]
        password = decode_str("utf-8")(decrypted[108:124])[0]
    except UnicodeDecodeError:
        return LoginFail(login.constants.LOGIN_FAIL_WRONG_LOGIN_OR_PASSWORD)

    try:
        account = await Account.one(username=username, required=False)
        if account is None:
            account = await Account.new(username=username, password=password)
        print(account)
        if not account.authenticate(password):
            raise WrongCredentials("Wrong Password")
    except WrongCredentials:
        return LoginFail(reason_id=login.constants.LOGIN_FAIL_WRONG_LOGIN_OR_PASSWORD)
    except ApiException:
        return LoginFail(reason_id=login.constants.LOGIN_FAIL_DATABASE_ERROR)
    except Exception as e:
        LOG.exception(e)
        return LoginFail(reason_id=login.constants.LOGIN_FAIL_WRONG_PASSWORD)

    request.session.set_state(Authenticated)
    request.session.account = account

    return LoginOk(
        login_ok1=request.session.session_key.login_ok1,
        login_ok2=request.session.session_key.login_ok2,
    )


@l2_request_handler(login.constants.REQUEST_GG_AUTH, Template([]), states=[Connected])
async def gg_authenticated(request):
    request.session.set_state(GGAuthenticated)
    return GGAuth()


@l2_request_handler(
    login.constants.REQUEST_SERVER_LIST,
    Template(
        [
            Parameter(id="login_ok1", start=0, length=4, type=ctype.int32),
            Parameter(id="login_ok2", start=4, length=4, type=ctype.int32),
        ]
    ),
    states=[Authenticated],
)
@verify_secrets
async def server_list(request):
    game_servers = await GameServer.all()
    request.session.set_state(WaitingGameServerSelect)
    return ServerList(servers=game_servers)


@l2_request_handler(
    login.constants.REQUEST_SERVER_LOGIN,
    Template(
        [
            Parameter(id="login_ok1", start=0, length=4, type=ctype.int32),
            Parameter(id="login_ok2", start=4, length=4, type=ctype.int32),
            Parameter(id="server_id", start=8, length=1, type=ctype.int8),
        ]
    ),
    states=[WaitingGameServerSelect],
)
@verify_secrets
async def server_login(request):
    game_server = await GameServer.one(
        server_id=request.validated_data["server_id"], required=False
    )

    if game_server is None:
        return PlayFail(reason_id=login.constants.PLAY_FAIL_ACCESS_DENIED)

    if game_server.is_full:
        return PlayFail(reason_id=login.constants.PLAY_FAIL_TOO_MANY_USERS)

    request.session.send_packet(
        PlayOk(
            play_ok1=request.session.session_key.play_ok1,
            play_ok2=request.session.session_key.play_ok2,
        )
    )

    await request.session.account.login_authenticated(
        game_server.id,
        request.session.session_key.play_ok1,
        request.session.session_key.play_ok2,
        request.session.session_key.login_ok1,
        request.session.session_key.login_ok2,
    )
