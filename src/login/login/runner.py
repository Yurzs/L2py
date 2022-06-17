import logging

from src.login.login.application import LOGIN_SERVER_APPLICATION
from src.login.login.config import (
    LOGIN_SERVER_API_HOST,
    LOGIN_SERVER_API_PORT,
    LOGIN_SERVER_HOST,
    LOGIN_SERVER_PORT,
    loop,
)

LOG = logging.getLogger(f"L2py.login")


def login_runner():
    LOGIN_SERVER_APPLICATION.run(
        {
            "login_web": {
                "host": LOGIN_SERVER_API_HOST,
                "port": LOGIN_SERVER_API_PORT,
            },
            "login_tcp": {
                "host": LOGIN_SERVER_HOST,
                "port": LOGIN_SERVER_PORT,
            },
        },
        loop=loop,
        log_level=logging.DEBUG,
    )


if __name__ == "__main__":
    login_runner()
