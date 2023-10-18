from aiohttp.web import (
    FileResponse,
    Request,
)

from utils import create_convert_file
from decorators import handler_exceptions
from validator import Validator
from logger import get_logger

logger = get_logger()


@handler_exceptions
async def convert_file(request: Request):
    request_data = await request.post()

    Validator(data=request_data).validate_data()
    file, convert_type = request_data.get('file'), request_data.get('to_type', 'pdf')

    file_content = file.file.read()
    _, file_type = file.filename.split('.')

    path = await create_convert_file(
        data=file_content,
        from_type=file_type,
        to_type=convert_type
    )

    return FileResponse(path)
