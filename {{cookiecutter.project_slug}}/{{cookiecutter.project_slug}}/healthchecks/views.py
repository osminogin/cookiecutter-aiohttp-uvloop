from datetime import datetime
from aiohttp import web


class PingCheckView(web.View):
    """
    Ping-pong view.
    """
    async def get(self):
        return web.Response(body=b'pong')


class HealthCheckView(web.View):
    """
    Health checks view.
    """
    async def get(self):
        postgres_health = await self._check_postgres()
        redis_health = await self._check_redis()
        uptime = await self._check_uptime()
        # Returns JSON-response from dict
        return web.json_response({
            'postgres': postgres_health,
            'redis': redis_health,
            'uptime': uptime
        })

    async def _check_postgres(self) -> bool:
        async with self.request.app.postgres.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute('SELECT 1')   # example request
                ret = []
                async for row in cur:
                    ret.append(row)
                return ret == [(1,)]

    async def _check_redis(self) -> bool:
        """ Checks Redis server key read/write. """
        await self.request.app.redis.set('IS_STARTED', '1')
        redis_health = await self.request.app.redis.get('IS_STARTED')
        return redis_health == '1'

    async def _check_uptime(self) -> int:
        """ Server uptime in seconds. """
        uptime = datetime.utcnow() - self.request.app.started
        return int(uptime.total_seconds())
