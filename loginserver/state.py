class State:
    pass


class Connected(State):
    pass


class GGAuthenticated(State):
    pass


class WaitingGGAccept(State):
    pass


class Authenticated(State):
    pass


class WaitingAuthenticationAccept(State):
    pass


class WaitingGameServerSelect(State):
    pass


class GameServerSelected(State):
    pass