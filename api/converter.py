from aiohttp.web import (
    FileResponse,
    Request,
)

from error_handlers import error_response
from utils import create_convert_file
from decorators import handler_exceptions
from validator import Validator
from logger import get_logger
from exceptions import (
    ConversionError,
    NotValidRequestData,
)

logger = get_logger()


@handler_exceptions
async def convert_file(request: Request):
    try:
        request_data = await request.post()

        Validator(data=dict(request_data)).validate_data()

        file, convert_type = request_data.get('file'), request_data.get('to_type', 'pdf')
        file_content, file_type = file.file.read(), file.filename.split('.')[1]

        path = await create_convert_file(
            data=file_content,
            from_type=file_type,
            to_type=convert_type
        )

    except NotValidRequestData as ex:
        logger.error(ex.message)
        return error_response(ex.message)
    except ConversionError as ex:
        logger.error(f'Ошибка конвертации! {ex.message}')
        return error_response('Ошибка конвертации!')

    return FileResponse(path)
