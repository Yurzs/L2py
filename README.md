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

Feel free to contribute. [Trello desk](https://trello.com/b/DjgolGFw/l2py)

How to start developing
-----------------------

- Run mongo on localhost
- Create account in mongo according to Login Account structure
- Start runner with env variable MONGO_URI
- Login using l2 client

Emulator servers architecture
----------------

Each server have a JSON api via which they communicate. 
Game and login servers are just network wrappers of L2 world.  
All events hapen in data server. Such architecture will allow load balancing between LS and GS instances.
