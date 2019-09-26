from datetime import datetime, date
from aiohttp import web


class PingCheckView(web.View):
    async def get(self):
        redis_health = await self._check_redis()
        uptime = await self._check_uptime()
        return web.json_response({
            'redis': redis_health,
            'uptime': uptime
        })

    async def _check_redis(self) -> bool:
        await self.request.app.redis.set('IS_STARTED', '1')
        redis_health = await self.request.app.redis.get('IS_STARTED')
        return redis_health == '1'

    async def _check_uptime(self) -> int:
        uptime = datetime.utcnow() - self.request.app.started
        return int(uptime.total_seconds())
