#!/usr/bin/env python3

"""A simple manual test for aiohttp_index. Specifying --occlude-root should stop /index.html
from being served."""

import argparse
from pathlib import Path
import sys

from aiohttp import web

APP_PATH = Path(__file__).parent

sys.path.append(str(APP_PATH.parent.parent))
from aiohttp_index import IndexMiddleware


def make_handler(s):
    async def handler(request):
        return web.Response(text=s)
    return handler


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--occlude-root', action='store_true',
                        help='Add an explicit handler function for /.')
    args = parser.parse_args()
    app = web.Application(middlewares=[IndexMiddleware()])
    app.router.add_route('GET', '/test/', make_handler('test'))
    if args.occlude_root:
        app.router.add_route('GET', '/', make_handler('I occluded /index.html.'))
    app.router.add_static('/', APP_PATH / 'static')

    web.run_app(app)

if __name__ == '__main__':
    main()
