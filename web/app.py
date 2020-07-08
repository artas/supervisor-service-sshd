from aiohttp import web
import aiohttp_jinja2
import jinja2
from .routes import setup_rotes


async def create_app():
    app = web.Application()
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.PackageLoader('web', 'templates')
    )
    setup_rotes(app)
    return app



