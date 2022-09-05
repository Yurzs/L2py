import copy
import functools
import logging

from common.request import Request
from common.response import Response
from game.request import GameRequest

_HANDLERS = {}


LOG = logging.getLogger(f"l2py.{__name__}")


def parse_data(request_template, f):
    async def wrap(request: Request):
        template = copy.deepcopy(request_template)
        request.validated_data = template.parse_request(request.data)
        return await f(request)

    return wrap


def l2_request_handler(action, template, states="*"):
    def wrapper(f):
        @functools.wraps(f)
        def inner(request, *args, **kwargs):
            LOG.info(
                "Request from %s: %s[%s] %s",
                request.session.uuid,
                f.__name__,
                action,
                request.validated_data,
            )
            return f(request, *args, **kwargs)

        _HANDLERS[action] = {
            "handler": parse_data(template, inner),
            "states": states,
        }
        return inner

    return wrapper


async def handle_request(request: GameRequest):
    action_id, request.data = request.data[0], bytearray(request.data[1:])
    LOG.debug("Looking for action with ID %s", action_id)
    if action_id in _HANDLERS:
        params = _HANDLERS[action_id]
        if params["states"] == "*" or request.session.state in params["states"]:
            result = await params["handler"](request)
            if result is None:
                return
            if isinstance(result, Response):
                return result
            return Response(packet=result, session=request.session)
