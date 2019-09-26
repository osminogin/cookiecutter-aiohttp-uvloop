import aioredis
from aiohttp import web

from .settings import *  # noqa
from .healthcheck.routes import register_routes as register_heathcheck_routes
from .utils import get_middlewares, get_version


def build_app(loop=None):
    app = web.Application(loop=loop, middlewares=get_middlewares())
    app.on_startup.append(load_plugins)
    app.on_cleanup.append(cleanup_plugins)
    register_routes(app)
    return app


def register_routes(app):
    register_heathcheck_routes(app)


async def load_plugins(app):
    version = await get_version()
    app.version = version

    redis = await aioredis.create_redis_pool(
        REDIS_URL,
        maxsize=REDIS_POOLSIZE or 10,
        timeout=60,
        encoding='utf-8',
        loop=app.loop
    )
    app.redis = redis


async def cleanup_plugins(app):
    app.redis.close()
