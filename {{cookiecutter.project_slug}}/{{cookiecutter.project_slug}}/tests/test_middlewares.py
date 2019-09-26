class TestVersion:

    async def test_version_middleware(self, app, client):
        response = await client.get('/ping/')
        assert response.status == 200
        assert response.headers.get('X-API-Version') == app.version
