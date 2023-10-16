from error_handlers import error_response
from logger import get_logger

logger = get_logger()


def handler_exceptions(func):
    async def inner_function(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            logger.error(e)
            return error_response(str(e))

    return inner_function
