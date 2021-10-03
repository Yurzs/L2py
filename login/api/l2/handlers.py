import functools


def verify_secrets(f):
    @functools.wraps(f)
    async def wrap(request, *args, **kwargs):
        request.session.session_key.verify_login(
            request.validated_data["login_ok1"], request.validated_data["login_ok2"]
        )
        return await f(request, *args, **kwargs)

    return wrap
