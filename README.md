cookiecutter-aiohttp-uvloop
===========================
[![](https://img.shields.io/github/release/osminogin/cookiecutter-aiohttp-uvloop.svg?style=flat)](https://github.com/osminogin/cookiecutter-aiohttp-uvloop/releases/latest) ![python 3.6, 3.7](https://img.shields.io/badge/python-3.6,%203.7-green.svg?style=flat) ![LICENSE.md](https://img.shields.io/badge/license-MIT-green.svg) [![Requirements Status](https://requires.io/github/osminogin/cookiecutter-aiohttp-uvloop/requirements.svg?branch=master)](https://requires.io/github/osminogin/cookiecutter-aiohttp-uvloop/requirements/?branch=master)

A [cookiecutter](https://github.com/audreyr/cookiecutter) project template for aiohttp on uvloop workers.

Features
--------
- Python 3.6, 3.7 support (latest available versions).
- Gunicorn with UVloop asyncio event loop built on top of libuv ([read why](http://magic.io/blog/uvloop-blazing-fast-python-networking/).
- Docker and docker-compose support.
- Pipenv for Python dependency management.

Usage
-----

```bash
pip3 install --user cookiecutter pipenv
export PATH $PATH:$HOME/.local/bin
cookiecutter gh:osminogin/cookiecutter-aiohttp-uvloop
# Run from docker
docker run --rm --publish 8000:8000 -i osminogin/cookiecutter-aiohttp-uvloop
# or all stack
docker-compose up
# or altenativly ...
...
```

License
-------

See [LICENSE.md](https://github.com/osminogin/cookiecutter-aiohttp-uvloop/blob/master/LICENSE.md).
