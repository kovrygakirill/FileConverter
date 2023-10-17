import asyncio
import aiofiles

from aiofiles import os

from exceptions import ConversionError


async def get_convert_file_data(
        data: bytes,
        from_type: str,
        to_type: str,
) -> bytes:
    async with aiofiles.tempfile.NamedTemporaryFile(
            dir='',
            suffix=f'.{from_type}'
    ) as tmp_file:
        await tmp_file.write(data)

        try:
            path = ''
            process = await asyncio.create_subprocess_exec(
                *['libreoffice', '--headless', '--convert-to', to_type, tmp_file.name],
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            _, error = await process.communicate()

            if error:
                raise ConversionError(f'Ошибка конвертации! {error.decode()}')

            path = tmp_file.name.split('.')[0] + f'.{to_type}'
            data = await get_created_file_content(path_to_file=path)
        finally:
            if path:
                await os.remove(path)

    return data


async def get_created_file_content(path_to_file: str) -> bytes:
    async with aiofiles.open(path_to_file, 'rb') as f:
        return await f.read()
