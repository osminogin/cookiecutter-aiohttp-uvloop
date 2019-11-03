import os
from urllib.parse import urlparse

import aiofiles

from .middlewares.version import version_middleware


def get_middlewares() -> tuple:
    return (version_middleware,)


async def get_version() -> str:
    async with aiofiles.open('VERSION', mode='r') as f:
        version = await f.read()
    return version.rstrip()


async def fetch(session, url, destination=None) -> None:
    """ Fetch URL file to destination path. """
    async with session.get(url) as response:
        response.raise_for_status()     # Throw exception if not HTTP OK

        # If destination path not specified - take filename from URL
        if not destination:
            parsed_url = urlparse(url)
            destination = os.path.basename(parsed_url.path)

        # Async write response to local file
        async with aiofiles.open(destination, mode='wb') as f:
            assert await f.write(await response.content.read())


async def parse_json(session, url, headers=None) -> (dict, list):
    """ Fetch URL and return native object from JSON. """
    async with session.get(url, headers=headers) as response:
        # Check valid `Content-Type` for JSON response
        assert response.content_type == 'application/json'
        return await response.json()
