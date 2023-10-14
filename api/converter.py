from aiofiles import os
from aiohttp.web import (
    json_response,
    Response,
    Request,
)

from utils import (
    create_convert_file,
    get_converted_file_content,
)


# from logger import get_logger

# logger = get_logger()


# @handler_exceptions
async def convert_file(request: Request):
    data = await request.post()
    file, convert_type = data.get('file'), data.get('type', 'pdf')

    if file is None:
        return json_response({'error': 'Переданный файл не найден!'})

    file_content = file.file.read()
    _, file_type = file.filename.split('.')

    path, error = await create_convert_file(
        data=file_content,
        from_type=file_type,
        to_type=convert_type
    )
    if error:
        return json_response({'error': f'Ошибка конвертацмм. {error}'})

    data = await get_converted_file_content(path_to_file=path)
    await os.remove(path)

    return Response(
        body=data,
        content_type='application/pdf'
    )
