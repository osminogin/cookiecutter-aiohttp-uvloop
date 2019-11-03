from datetime import datetime

{% if cookiecutter.use_postgres == 'y' -%}import aiopg{%- endif -%}
{% if cookiecutter.use_redis == 'y' -%}import aioredis{%- endif %}
from aiohttp import web

from .settings import *  # noqa
from .utils import get_middlewares, get_version
from .healthchecks.views import PingCheckView, HealthCheckView


def build_app(argv=None) -> web.Application:
    app = web.Application(middlewares=get_middlewares())
    app.on_startup.append(startup_handler)
    app.on_cleanup.append(cleanup_handler)
    register_routes(app)
    return app


def register_routes(app) -> None:
    app.router.add_route('*', '/ping/', PingCheckView)
    app.router.add_route('*', '/health/', HealthCheckView)


async def startup_handler(app) -> None:
    # Additional data
    app.started = datetime.utcnow()
    app.version = await get_version()

    {% if cookiecutter.use_postgres == 'y' -%}
    # PostgreSQL connection pool
    dsn = f"dbname={PGDATABASE} user={PGUSER} password={PGPASSWORD} host={PGHOST}"
    postgres = await aiopg.create_pool(dsn)
    app.postgres = postgres
    {%- endif -%}

    {% if cookiecutter.use_redis == 'y' -%}
    # Redis pool
    redis = await aioredis.create_redis_pool(
        address=REDIS_URL,
        maxsize=int(REDIS_POOLSIZE) or 10,
        timeout=int(REDIS_TIMEOUT) or 60,
        encoding='utf-8',
        loop=app.loop
    )
    app.redis = redis
    {%- endif %}


async def cleanup_handler(app) -> None:
    """ Cleanup on exit. """
    {% if cookiecutter.use_postgres == 'y' -%}
    app.postgres.close()
    await app.postgres.wait_closed()
    {%- endif -%}

    {% if cookiecutter.use_redis == 'y' -%}
    app.redis.close()
    await app.redis.wait_closed()
    {%- endif %}

