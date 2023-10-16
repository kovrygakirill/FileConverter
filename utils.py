import asyncio
import aiofiles


async def create_convert_file(
        data: bytes,
        from_type: str,
        to_type: str,
) -> tuple[str, str]:
    async with aiofiles.tempfile.NamedTemporaryFile(
            dir='',
            suffix=f'.{from_type}'
    ) as tmp_file:
        await tmp_file.write(data)

        process = await asyncio.create_subprocess_exec(
            *['libreoffice', '--headless', '--convert-to', to_type, tmp_file.name],
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        _, error = await process.communicate()

    path = tmp_file.name.split('.')[0] + f'.{to_type}'

    return path, error.decode()


async def get_converted_file_content(path_to_file: str) -> bytes:
    async with aiofiles.open(path_to_file, 'rb') as f:
        return await f.read()
