class TestVersion:

    async def test_version_middleware(self, app, event_loop, aiohttp_client):
        client = await aiohttp_client(event_loop)
        response = await client.get('/ping/')
        assert response.status == 200
        assert response.headers.get('X-API-Version') == app.version
