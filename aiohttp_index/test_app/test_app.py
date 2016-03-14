#!/usr/bin/env python3

from pathlib import Path
import sys

from aiohttp import web

APP_PATH = Path(__file__).parent
sys.path.append(str(APP_PATH / '../..'))
from aiohttp_index import IndexMiddleware


async def handler(request):
    return web.Response(text='hi')

app = web.Application(middlewares=[IndexMiddleware()])
# app.router.add_route('GET', '/', handler)
app.router.add_static('/', APP_PATH / 'static')

web.run_app(app)
