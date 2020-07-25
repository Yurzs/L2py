import logging

from common.client.exceptions import ApiException, WrongCredentials
from common.client.data_client import DataClient
from common.manager import PacketManager
from mdocument import DocumentDoesntExist

from loginserver.config import data_server_connection_info
from loginserver.session_storage import session_storage
from .packets.from_server import GGAuth, LoginFail, LoginOk, PlayFail, PlayOk, ServerList
from .state import Authenticated, Connected, GameServerSelected, GGAuthenticated, \
    WaitingGameServerSelect

LOG = logging.getLogger(f"l2py-server-login.{__name__}")


class LoginServerPacketManager(PacketManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_client = DataClient(*data_server_connection_info)

    async def proceed(self, client: "LoginClient", packet):
        if not packet:
            return client.protocol.transport._transport.close()
        if isinstance(client.state, Connected):
            reply = GGAuth()
            client.state = GGAuthenticated()
            return reply
        elif isinstance(client.state, GGAuthenticated):
            try:
                account = await self.data_client.get_account(packet.login.value,
                                                             packet.password.value)
                reply = LoginOk(client.session_key.login_ok1, client.session_key.login_ok2)
                client.state = Authenticated()
                client.account = account
            except WrongCredentials as e:
                LOG.warning(e.message)
                reply = LoginFail(LoginFail.REASON.WRONG_LOGIN_OR_PASSWORD)
            except ApiException as e:
                LOG.error(e.message)
                reply = LoginFail(LoginFail.REASON.DATABASE_ERROR)
            return reply
        elif isinstance(client.state, Authenticated):
            if client.session_key.verify_login(packet.login_ok1, packet.login_ok2):
                try:
                    game_servers = await self.data_client.get_server_list()
                    reply = ServerList(game_servers)
                    client.state = WaitingGameServerSelect()
                except DocumentDoesntExist:
                    client.state = WaitingGameServerSelect()
                    reply = ServerList()
            else:
                reply = ServerList()
            return reply
        elif isinstance(client.state, WaitingGameServerSelect):
            if client.session_key.verify_login(packet.login_ok1, packet.login_ok2):
                try:
                    gs = await self.data_client.get_server(packet.server_id.value)
                    await self.data_client.set_account_latest_server(client.account["login"],
                                                                     gs["id"])
                    reply = PlayOk(client.session_key.play_ok1, client.session_key.play_ok2)
                    client.state = GameServerSelected()
                    session_storage[client.account["login"]] = client.session_key.to_dict()
                except ApiException as e:
                    reply = PlayFail(PlayFail.REASON.ACCESS_DENIED)
                    LOG.exception(e.message)
            else:
                reply = PlayFail(PlayFail.REASON.ACCESS_DENIED)
            return reply
