import aiofiles
from asyncio import subprocess


async def create_convert_file(
        data,
        from_type,
        to_type,
):
    async with aiofiles.tempfile.NamedTemporaryFile(
            dir='',
            suffix=f'.{from_type}'
    ) as tmp_file:
        await tmp_file.write(data)

        process = await subprocess.create_subprocess_exec(
            *['libreoffice', '--headless', '--convert-to', to_type, tmp_file.name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        _, error = await process.communicate()

    path = tmp_file.name.split('.')[0] + f'.{to_type}'

    return path, error


async def get_converted_file_content(path_to_file: str):
    async with aiofiles.open(path_to_file, 'rb') as f:
        return await f.read()
