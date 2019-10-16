import pytest


class TestPingHealthCheck:

    @pytest.fixture
    def close_redis(self, app):
        app.redis.close()

        yield

        for c in app.redis._connections:
            app.loop.run_until_complete(c._reconnect())

    async def test_health_success(self, aiohttp_client, event_loop, app):
        client = await aiohttp_client(app)
        response = await client.get('/health/')
        assert response.status == 200

        content = await response.json()
        assert content['redis'] is True
        assert content['postgres'] is True
        assert content['uptime'] > 0

    async def test_ping_success(self, client):
        response = await client.get('/ping/')
        assert response.status == 200

        content = await response.text()
        assert content == 'pong'

    async def test_ping_fail(self, client, close_redis):
        response = await client.get('/health/')
        assert response.status == 500
