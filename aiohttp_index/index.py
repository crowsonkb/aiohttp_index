"""Middleware to serve index files (e.g. index.html) when static directories are requested."""

__all__ = ['IndexMiddleware']


def IndexMiddleware(index='index.html'):
    """Middleware to serve index files (e.g. index.html) when static directories are requested.

    Usage:
    ::

       from aiohttp_index import IndexMiddleware
       app = web.Application(middlewares=[IndexMiddleware()])
       app.router.add_static('/', 'static')

    ``app`` will now serve ``static/index.html`` when ``/`` is requested.

    :param str index: The name of a directory's index file.
    :returns: The middleware factory.
    :rtype: function
    """
    async def middleware_factory(app, handler):
        """Middleware factory method.

        :type app: aiohttp.web.Application
        :type handler: function
        :returns: The retry handler.
        :rtype: function
        """
        async def index_handler(request):
            """Handler to serve index files (index.html) for static directories.

            :type request: aiohttp.web.Request
            :returns: The result of the next handler in the chain.
            :rtype: aiohttp.web.Response
            """
            try:
                filename = request.match_info['filename']
                if not filename:
                    filename = index
                if filename.endswith('/'):
                    filename += index
                request.match_info['filename'] = filename
            except KeyError:
                pass
            return await handler(request)
        return index_handler
    return middleware_factory
