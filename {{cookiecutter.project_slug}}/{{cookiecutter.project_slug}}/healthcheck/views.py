from aiohttp import web


class PingCheckView(web.View):
    async def get(self):
        redis_health = await self._check_redis()
        return web.json_response({
            'redis': redis_health
        })

    async def _check_redis(self) -> bool:
        await self.request.app.redis.set('IS_STARTED', '1')
        redis_health = await self.request.app.redis.get('IS_STARTED')
        return redis_health == '1'


    async  def _check_uptime)
