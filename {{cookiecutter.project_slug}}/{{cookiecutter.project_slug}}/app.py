from datetime import datetime

import aiopg
import aioredis
from aiohttp import web

from .settings import *  # noqa
from .utils import get_middlewares, get_version
from .healthchecks.views import PingCheckView, HealthCheckView


def build_app(loop=None):
    app = web.Application(loop=loop, middlewares=get_middlewares())
    app.on_startup.append(load_extensions)
    app.on_cleanup.append(cleanup_extensions)
    register_routes(app)
    return app


def register_routes(app) -> None:
    app.router.add_route('*', '/ping/', PingCheckView)


async def load_extensions(app) -> None:
    # Additional data
    app.started = datetime.utcnow()
    app.version = await get_version()

    # PostgreSQL connection pool
    dsn = f"dbname=postgres user=postgres password=postgres host=127.0.0.1"
    postgres = await aiopg.create_pool(dsn)
    app.postgres = postgres

    # Redis pool
    redis = await aioredis.create_redis_pool(
        address=REDIS_URL,
        maxsize=REDIS_POOLSIZE or 10,
        timeout=REDIS_TIMEOUT or 60,
        encoding='utf-8',
        loop=app.loop
    )
    app.redis = redis


async def cleanup_extensions(app) -> None:
    app.redis.close()
    await app.redis.wait_closed()

    app.postgres.close()
    await app.postgres.wait_closed()
