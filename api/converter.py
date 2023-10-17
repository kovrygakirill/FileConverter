from aiohttp.web import (
    Response,
    Request,
)

from utils import get_convert_file_data
from decorators import handler_exceptions
from validator import Validator
from logger import get_logger
from settings import CONVERT_FILE_TYPES

logger = get_logger()


@handler_exceptions
async def convert_file(request: Request):
    request_data = await request.post()

    Validator(data=request_data).validate_data()
    file, convert_type = request_data.get('file'), request_data.get('type', 'pdf')

    file_content = file.file.read()
    _, file_type = file.filename.split('.')

    data = await get_convert_file_data(
        data=file_content,
        from_type=file_type,
        to_type=convert_type
    )

    return Response(
        body=data,
        content_type=CONVERT_FILE_TYPES[convert_type]
    )
