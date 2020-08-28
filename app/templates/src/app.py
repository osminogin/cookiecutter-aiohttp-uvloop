from datetime import datetime

<% if (use_postgres) { %>import aiopg<% } %>
<% if (use_redis) { %>import aioredis<% } %>
from aiohttp import web

from .settings import *  # noqa
from .utils import get_middlewares, get_version
from .healthcheck.views import PingCheckView, HealthCheckView


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

    <%_ if (use_postgres) { _%>
    # PostgreSQL connection pool
    dsn = f"dbname={PGDATABASE} user={PGUSER} password={PGPASSWORD} host={PGHOST}"
    postgres = await aiopg.create_pool(dsn)
    app.postgres = postgres
    <%_ } _%>

    <%_ if (use_redis) { _%>
    # Redis pool
    redis = await aioredis.create_redis_pool(
        address=REDIS_URL,
        maxsize=int(REDIS_POOLSIZE) or 10,
        timeout=int(REDIS_TIMEOUT) or 60,
        encoding='utf-8',
        loop=app.loop
    )
    app.redis = redis
    <%_ } _%>


async def cleanup_handler(app) -> None:
    """ Cleanup on exit. """
    <%_ if (use_postgres) { _%>
    app.postgres.close()
    await app.postgres.wait_closed()
    <%_ } _%>
    <%_ if (use_redis) { _%>
    app.redis.close()
    await app.redis.wait_closed()
    <%_ } _%>

