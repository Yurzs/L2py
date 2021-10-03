l2py
====
Lineage2 Interlude+ server emulator written in python3

Stage: Alpha

What currently works
--------------------
- [x] Login Server
- [ ] Game Server


Contribute
----------

Feel free to join developing our server:
* If you have some suggestions - please [open an Issue](https://github.com/Yurzs/L2py/issues/new/choose).
* If you want to implement some features - check [Project page](https://github.com/Yurzs/L2py/projects/1).

How to start developing
-----------------------

- Run mongo on localhost
- Create account in mongo according to Login Account structure
- Start runner with env variable `MONGO_URI=localhost`
- Login using l2 client

Emulator server architecture
----------------

Project is split to 3 components:

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
