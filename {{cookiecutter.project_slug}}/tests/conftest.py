import pytest

from .. import app as _app
from .. import loop as _loop


@pytest.fixture
def app(event_loop):
    return _app


@pytest.fixture
def client(event_loop, aiohttp_client, app):
    return event_loop.run_until_complete(aiohttp_client(app))
