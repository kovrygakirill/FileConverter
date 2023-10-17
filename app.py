import asyncio
import uvloop

from aiohttp import web

from routes import routes
from settings import MAX_SIZE_CLIENT_DATA


async def get_app() -> web.Application:
    """Create AioHttp Application

    :returns
    web.Application: AioHttp Application
    """
    application = web.Application(client_max_size=MAX_SIZE_CLIENT_DATA)
    application.add_routes(routes)

    return application


if __name__ == '__main__':
    uvloop.install()
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(get_app())
    web.run_app(app, port=8080)
