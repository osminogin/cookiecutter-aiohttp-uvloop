import pytest


class TestHealthCheck:

    @pytest.fixture
    def close_redis(self, app):
        app.redis.close()

        yield

        for c in app.redis._connections:
            app.loop.run_until_complete(c._reconnect())

    @pytest.fixture
    def route(self):
        return '/ping/'

    async def test_ping_success(self, client, route):
        response = await client.get(route)
        assert response.status == 200

        content = await response.json()
        assert content['redis'] is True

    async def test_ping_fail(self, client, close_redis, route):
        response = await client.get(route)
        assert response.status == 500
