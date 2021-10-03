import logging
import aiojsonapi.config

import login.api.http  # noqa: F401
import login.api.l2  # noqa: F401
from login.application import LOGIN_SERVER_APPLICATION
from login.config import (
    SERVER_API_HOST,
    SERVER_API_PORT,
    SERVER_HOST,
    SERVER_PORT,
    loop,
)
from login.session import LoginSession

LOG = logging.getLogger(f"L2py.login")


def main():
    LoginSession.start()
    LOGIN_SERVER_APPLICATION.run(
        {
            "login_web": {
                "host": SERVER_API_HOST,
                "port": SERVER_API_PORT,
            },
            "login_tcp": {
                "host": SERVER_HOST,
                "port": SERVER_PORT,
            },
        },
        loop=loop,
        log_level=logging.DEBUG,
    )


if __name__ == "__main__":
    main()
