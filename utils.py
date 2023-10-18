import asyncio
import aiofiles

from exceptions import ConversionError
from settings import CONVERTED_FILES_DIR


async def create_convert_file(
        data: bytes,
        from_type: str,
        to_type: str,
) -> str:
    async with aiofiles.tempfile.NamedTemporaryFile(
            dir=CONVERTED_FILES_DIR,
            suffix=f'.{from_type}'
    ) as tmp_file:
        await tmp_file.write(data)

        process = await asyncio.create_subprocess_exec(
            *['libreoffice', '--headless', '--convert-to', to_type, '--outdir', CONVERTED_FILES_DIR, tmp_file.name],
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        _, error = await process.communicate()

        if error:
            raise ConversionError(f'Ошибка конвертации! {error.decode()}')

        path = tmp_file.name.split('.')[0] + f'.{to_type}'

    return path
