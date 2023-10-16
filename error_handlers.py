from aiohttp.web import json_response


def error_response(error_text: str):
    return json_response(
        data={'error': error_text},
        status=400
    )
