import asyncio

from aiohttp import web

from {{cookiecutter.project_slug}} import build_app


async def test_ping_success(aiohttp_client) -> None:
    """ Проверка тестового метода ping-pong. """
    client = await aiohttp_client(build_app)
    response = await client.get('/ping')
    assert response.status == web.HTTPOk.status_code
    content = await response.text()
    assert response.content_type == 'text/plain'
    assert content == 'pong'


async def test_healthcheck_success(aiohttp_client):
    """ Проверка аптайма (специально делаем задержку в 1s). """
    client = await aiohttp_client(build_app)
    response = await client.get('/health')
    assert response.status == web.HTTPOk.status_code
    assert response.content_type == 'application/json'
    data = await response.json()
    sleep = await asyncio.sleep(1)  # Timeout 1 second
    assert 'uptime' in data
    assert not sleep, data['uptime'] > 0
