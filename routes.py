from aiohttp import web

from api import converter

routes = [
    web.post('/convert', converter.convert_file),
]
