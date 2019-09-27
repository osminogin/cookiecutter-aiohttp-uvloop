cookiecutter-aiohttp-uvloop
===========================
[![](https://img.shields.io/github/release/osminogin/cookiecutter-aiohttp-uvloop.svg?style=flat)](https://github.com/osminogin/cookiecutter-aiohttp-uvloop/releases/latest) ![python 3.7](https://img.shields.io/badge/python-3.7-green.svg?style=flat) ![LICENSE.md](https://img.shields.io/badge/license-MIT-green.svg) [![Requirements Status](https://requires.io/github/osminogin/cookiecutter-aiohttp-uvloop/requirements.svg?branch=master)](https://requires.io/github/osminogin/cookiecutter-aiohttp-uvloop/requirements/?branch=master)

A [cookiecutter](https://github.com/audreyr/cookiecutter) project template for aiohttp on uvloop workers.

Features
--------
- Python 3.7 support (latest available version).
- Gunicorn with UVloop worker class.
- Docker and docker-compose support.
- Pipenv for Python dependency management.

Usage
-----

```bash
pip3 install --user cookiecutter pipenv
${HOME}/.local/bin/cookiecutter https://github.com/osminogin/cookiecutter-aiohttp-uvloop.git
# Run from docker
# XXX:
```

License
-------

See [LICENSE.md](https://github.com/osminogin/cookiecutter-aiohttp-uvloop/blob/master/LICENSE.md).
