generator-aiohttp-uvloop
========================
![Python 3.6, 3.7, 3.8](https://img.shields.io/badge/python-3.6,%203.7,%203.8-green.svg?style=flat) [![LICENSE](https://img.shields.io/badge/License-MIT-black.svg)](https://github.com/osminogin/generator-aiohttp-uvloop/blob/master/LICENSE)

A [generator](https://github.com/audreyr/generator) project template for aiohttp on uvloop workers.

Features
--------
- Python 3.6, 3.7, 3.8 supported.
- Pipenv for dependency management.
- Gunicorn with UVloop asyncio event loop built on top of libuv ([read why](http://magic.io/blog/uvloop-blazing-fast-python-networking/)).
- Docker and docker-compose support.
- Heroku deployment support.

Usage
-----

```bash
sudo pip3 install --upgrade generator pipenv
generator gh:osminogin/generator-aiohttp-uvloop
# Run HTTP daemon
make daemon
# or with docker
docker run --rm --publish 8000:8000 -i osminogin/generator-aiohttp-uvloop
# or all stack
docker-compose up
# or altenativly run development server
make dev
```

License
-------

See [LICENSE](https://github.com/osminogin/generator-aiohttp-uvloop/blob/master/LICENSE)
