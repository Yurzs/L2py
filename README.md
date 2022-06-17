L2py
====

<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
<a href="https://discord.gg/hgdFQYxtvm"><img src="https://img.shields.io/discord/897633223608250388?logo=discord" alt="chat on Discord"></a>

Lineage2 Interlude+ server emulator written in python3

Stage: Alpha


What currently works
--------------------
- [x] Login Server
- [x] Game Server


Contribute
----------

Feel free to join developing our server:
* If you have some suggestions - please [open an Issue](https://github.com/Yurzs/L2py/issues/new/choose).
* If you want to implement some features - check [Project page](https://github.com/Yurzs/L2py/projects/1).
* Or join our [Discord server](https://discord.gg/hgdFQYxtvm)

How to start developing
=======================

* Copy `.env.example` to `.env`.
* Set environment variables as you need in `.env`

Using docker-compose
------------

* Build docker images `make docker-create`
* Start containers `docker-compose up -d`
* Register game server in database `make compose-exec-login register_game_server <GAME_SERVER_HOST> <GAME_SERVER_PORT> <GAME_SERVER_ID>`.

Without docker-compose
--------------

* Install poetry using `make install`
* Run `poetry install`
* Start mongodb in container or using other methods.
* Activate virtual environment `. .venv/bin/activate`
* Register game server in database `login/bin/register_game_server <GAME_SERVER_HOST> <GAME_SERVER_PORT> <GAME_SERVER_ID>`
* Start login server `python game_runner.py`
* Start game server `python login_runner.py`

Emulator server architecture
----------------

Project is split to 2 components:

- `Login Server` - L2 login service + basic HTTP API
- `Game Server` - L2 game service + basic HTTP API

All those services have own instances of `common.application.Application` 
with specific modules (for example game server have `TCPServerModule`, `HTTPServerModule`, `ScheduleModule`).

ApplicationModules
------------------

Each `ApplicationModule` adds functionality to main application process.
All modules are running in one asyncio loop.

- `TCPServerModule`: L2 protocol requests handler
- `HTTPServerModule`: HTTP JSON requests handler
- `ScheduleModule`: CRON tasks runner

TCPServerModule Middlewares
---------------------------

Middlewares are used in L2 protocol handler for convenient way for not caring
about all those complicated protocol specific encryption.

Data types
----------

Most of the custom data types derive from ctypes (At least numeric ones.)
