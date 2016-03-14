# aiohttp_index

[aiohttp.web](http://aiohttp.readthedocs.org/en/stable/) middleware to serve index files
(e.g. index.html) when static directories are requested.

## Usage
``` python
from aiohttp import web
from aiohttp_index import IndexMiddleware
app = web.Application(middlewares=[IndexMiddleware()])
app.router.add_static('/', 'static')
```

`app` will now serve `static/index.html` when `/` is requested.

## Dependencies

- Python 3.5+
- [aiohttp](http://aiohttp.readthedocs.org/en/stable/) (tested on 0.21.4)
