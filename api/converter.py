from aiofiles import os
from aiohttp.web import (
    Response,
    Request,
)

from utils import (
    create_convert_file,
    get_converted_file_content,
)
from decorators import handler_exceptions
from error_handlers import error_response
from logger import get_logger

logger = get_logger()


@handler_exceptions
async def convert_file(request: Request):
    data = await request.post()
    file, convert_type = data.get('file'), data.get('type', 'pdf')

    if file is None:
        logger.error('Переданный файл не найден!')
        return error_response('Переданный файл не найден!')

    file_content = file.file.read()
    _, file_type = file.filename.split('.')

    path, error = await create_convert_file(
        data=file_content,
        from_type=file_type,
        to_type=convert_type
    )
    if error:
        logger.error(f'Ошибка конвертации. {error}')
        return error_response('Ошибка конвертации.')

    data = await get_converted_file_content(path_to_file=path)
    await os.remove(path)

    return Response(
        body=data,
        content_type='application/pdf'
    )
