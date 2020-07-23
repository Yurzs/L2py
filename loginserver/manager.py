from mdocument import DocumentDoesntExist

from common.manager import PacketManager
from common.models import Account
from loginserver.config import auto_registration
from loginserver.models import GameServer
from loginserver.session_storage import session_storage
from .packets.from_server import GGAuth, LoginFail, LoginOk, PlayFail, PlayOk, ServerList
from .state import Authenticated, Connected, GameServerSelected, GGAuthenticated, \
    WaitingGameServerSelect


class LoginServerPacketManager(PacketManager):

    @classmethod
    async def proceed(cls, client: "LoginClient", packet):
        if not packet:
            return client.protocol.transport._transport.close()
        if isinstance(client.state, Connected):
            reply = GGAuth()
            client.state = GGAuthenticated()
            return reply
        elif isinstance(client.state, GGAuthenticated):
            try:
                account = await Account.authenticate(login=packet.login.value,
                                                     password=packet.password.value)
                if account is None:
                    reply = LoginFail(LoginFail.REASON.WRONG_LOGIN_OR_PASSWORD)
                elif account.can_login:
                    reply = LoginOk(client.session_key.login_ok1, client.session_key.login_ok2)
                    client.state = Authenticated()
                    client.account = account
                else:
                    reply = LoginFail(LoginFail.REASON.ACCESS_DENIED)
            except DocumentDoesntExist:
                if auto_registration:
                    account = await Account.create(packet.login.value, packet.password.value)
                    reply = LoginOk(client.session_key.login_ok1, client.session_key.login_ok2)
                    client.state = Authenticated()
                    client.account = account
                else:
                    reply = LoginFail(LoginFail.REASON.WRONG_LOGIN_OR_PASSWORD)
            return reply
        elif isinstance(client.state, Authenticated):
            if client.session_key.verify_login(packet.login_ok1, packet.login_ok2):
                try:
                    game_servers = await GameServer.many(public=True)
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
                    gs = await GameServer.one(id=packet.server_id.value)
                    client.account["latest_server"] = gs.id
                    reply = PlayOk(client.session_key.play_ok1, client.session_key.play_ok2)
                    client.state = GameServerSelected()
                    await client.account.push_update()
                    session_storage[client.account.login] = client.session_key.to_dict()
                except DocumentDoesntExist:
                    reply = PlayFail(PlayFail.REASON.ACCESS_DENIED)
            else:
                reply = PlayFail(PlayFail.REASON.ACCESS_DENIED)
            return reply
