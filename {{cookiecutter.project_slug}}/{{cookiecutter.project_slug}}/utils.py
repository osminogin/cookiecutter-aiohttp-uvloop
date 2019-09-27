import aiofiles

from .middlewares.version import version_middleware


def get_middlewares():
    return (version_middleware,)


async def get_version():
    async with aiofiles.open('VERSION', mode='r') as f:
        version = await f.read()
    return version
