from datetime import date, datetime

from aiohttp import web

from {{cookiecutter.project_slug}} import build_app
from {{cookiecutter.project_slug}}.utils import get_version


async def test_app_version():
    """ Проверка версии приложения и API. """
    version = await get_version()
    assert version == '0.1'


async def test_build_app(aiohttp_client) -> None:
    client = await aiohttp_client(build_app)
    app = client.app
    assert isinstance(app, web.Application)
    assert getattr(app, 'started')
    assert isinstance(app.started, date)
    assert datetime.utcnow() > app.started
    assert getattr(app, 'version')
    assert float(client.app.version)


async def test_not_found_method(aiohttp_client, auth) -> None:
    """ Not found method. """
    client = await aiohttp_client(build_app)
    response = await client.get('/abcde123', headers=auth)
    assert response.status == web.HTTPNotFound.status_code
