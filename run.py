from aiohttp import web
from web.app import create_app
import syslog

app = create_app()

web.run_app(app)