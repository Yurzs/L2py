import random

from mdocument import DocumentDoesntExist

from common.manager import Manager
from login_server.models import Account, GameServer
from .packets.from_server import GGAuth, LoginFail, LoginOk, PlayFail, PlayOk, ServerList
from .state import Authenticated, Connected, GGAuthenticated, WaitingGameServerSelect


class LoginManager(Manager):

    @classmethod
    async def proceed(cls, client, packet):
        if isinstance(client.state, Connected):
            reply = GGAuth()
            client.state = GGAuthenticated()
            return reply
        elif isinstance(client.state, GGAuthenticated):
            try:
                account = await Account.one(login=packet.login.value,
                                            password=packet.password.value)
                if account.can_login:
                    client.session_id1_1 = random.randrange(1, 2147483646)
                    client.session_id1_2 = random.randrange(1, 2147483646)
                    reply = LoginOk(client.session_id1_1, client.session_id1_2)
                    client.state = Authenticated()
                else:
                    reply = LoginFail(3)
            except DocumentDoesntExist:
                reply = LoginFail(3)
            return reply
        elif isinstance(client.state, Authenticated):
            if packet.session_id1 == client.session_id1_1 and \
                    packet.session_id2 == client.session_id1_2:
                try:
                    game_servers = await GameServer.many(public=True)
                    packet = ServerList(game_servers)
                    client.state = WaitingGameServerSelect()
                except DocumentDoesntExist:
                    client.state = WaitingGameServerSelect()
                    packet = ServerList({})
            else:
                packet = ServerList({})
            return packet
        elif isinstance(client.state, WaitingGameServerSelect):
            if packet.session_id1 == client.session_id1_1 and \
                    packet.session_id2 == client.session_id1_2:
                try:
                    server = await GameServer.one(id=packet.server_id.value)
                    client.session_id2_1 = random.randrange(1, 2147483646)
                    client.session_id2_2 = random.randrange(1, 2147483646)
                    packet = PlayOk(client.session_id2_1, client.session_id2_2)
                except DocumentDoesntExist:
                    packet = PlayFail(4)
            else:
                packet = PlayFail(4)
            print(packet.__dict__)
            return packet
