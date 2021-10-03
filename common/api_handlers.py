import functools

from common.helpers.bytearray import ByteArray
from common.request import Request
from common.response import Response

_HANDLERS = {}


def parse_data(template, f):
    async def wrap(request: Request):
        for parameter in template.parameters:
            start = template.get_start(parameter.id)
            if parameter.length is not None:
                chunk = ByteArray(request.data[start : start + parameter.length])
            elif parameter.stop is not None:
                chunk = ByteArray(request.data[start : parameter.stop])
            else:
                chunk = ByteArray(request.data[start:])
            parsed_value, stop = parameter.parse(chunk)
            template.set_stop(parameter.id, start + stop)
            request.validated_data[parameter.id] = parsed_value
        return await f(request)

    return wrap


def l2_request_handler(action, template, states="*"):
    def wrapper(f):
        @functools.wraps(f)
        def inner(*args, **kwargs):
            return f(*args, **kwargs)

        _HANDLERS[action] = {
            "handler": parse_data(template, f),
            "states": states,
        }
        return inner

    return wrapper


async def handle_request(request):
    action_id, request.data = request.data[0], ByteArray(request.data[1:])
    print(action_id)
    if action_id in _HANDLERS:
        params = _HANDLERS[action_id]
        if params["states"] == "*" or request.session.state in params["states"]:
            result = await params["handler"](request)
            if isinstance(result, Response):
                return result
            return Response(await params["handler"](request), request.session)
