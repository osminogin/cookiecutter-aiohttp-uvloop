generator-aiohttp-uvloop
========================
![Python 3.6, 3.7, 3.8](https://img.shields.io/badge/python-3.6,%203.7,%203.8-green.svg?style=flat) [![NPM Badge](https://img.shields.io/npm/v/generator-aiohttp-uvloop.svg)](https://www.npmjs.com/package/generator-aiohttp-uvloop) [![Licensed under MIT](https://img.shields.io/badge/license-MIT-black.svg)](https://github.com/osminogin/generator-aiohttp-uvloop/blob/master/LICENSE)

Generates a Python3 and [AIOHTTP](https://docs.aiohttp.org/en/stable) project with ultra fast [UVloop](https://github.com/MagicStack/uvloop) event loop.

## Features

- Gunicorn with UVloop asyncio event loop ([read why](http://magic.io/blog/uvloop-blazing-fast-python-networking/)).
- Pipenv for dependency management.
- Docker frendly (also docker-compose file included).
- Heroku deployment support.

## Requirements

- Python 3.6, 3.7 or 3.8
- Yeoman >= 4.11.0


## Generator installation
 
1) You are going to need [Yeoman](http://yeoman.io/):
```bash
npm install -g yo
```
2) Install the generator:

```bash
npm install -g generator-aiohttp-uvloop
```

## Usage

### Base generator

Create a new directory where you want your project to be and run it:

```bash
mkdir aio-service
cd aio-service
yo aiohttp-uvloop
```

License
-------

MIT. See [LICENSE](https://github.com/osminogin/generator-aiohttp-uvloop/blob/master/LICENSE)
