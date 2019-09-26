import asyncio

from .app import build_app
from .utils import get_version

loop = asyncio.get_event_loop()
app = build_app(loop)
__version__ = loop.run_until_complete(get_version)

