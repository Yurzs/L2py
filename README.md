L2py
====

<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
<a href="https://discord.gg/hgdFQYxtvm"><img src="https://img.shields.io/discord/897633223608250388?logo=discord" alt="chat on Discord"></a>

Lineage II Interlude+ server emulator written in python3

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
* Or join our [Discord server](https://discord.gg/AwV3yQKR)

How to start developing
-----------------------

Without `docker`:
- Install requirements with `make install_requirements` (Note: on macOS [`homebrew`](https://brew.sh/) is required)
- Install and start [`mongodb`](https://www.mongodb.com/) on localhost
- Copy `.env.example` to `.env`, change environment variables as needed
- Set up and activate venv with [`poetry`](https://python-poetry.org/) by `make install`
- Create a game server using `bin/register_game_server`
- Start `data`, `login`, `game` services with `poetry run python <service>/<service>/runner.py`

Using [`docker`](https://www.docker.com/):
- Install `docker` and `docker-compose` by [any preferred method](https://docs.docker.com/engine/install/)
- Edit `docker-compose.yml` as needed
- Run `make compose-build`, then `docker-compose up`

Emulator server architecture
----------------

Project is split into 3 components:

- `Login Server` - L2 login service + basic HTTP API
- `Game Server` - L2 game service + basic HTTP API
- `Data Server` - HTTP API which handles all DB communications

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

For readability improvement they've been added to globals (builtins). 

So to fix warnings in your IDE please add all data types from `common.datatypes` 
to your ignore unresolved list.
