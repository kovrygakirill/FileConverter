import os
import pathlib

MAX_SIZE_CLIENT_DATA = 1024 ** 3  # 1 GB

TEXT_DOCUMENTS = ['ODT', 'DOC', 'DOCX', 'RTF', 'TXT', 'HTML']
SPREADSHEETS = ['ODS', 'XLS', 'XLSX', 'CSV']
PRESENTATIONS = ['ODP', 'PPT', 'PPTX']
IMAGES = ['BMP', 'GIF', 'JPG', 'PNG', 'SVG']
OTHER_FORMATS = ['PDF', 'EPUB', 'SWF', 'XHTML']

AVAILABLE_FORMATS = TEXT_DOCUMENTS + SPREADSHEETS + PRESENTATIONS + IMAGES + OTHER_FORMATS


BASE_DIR = pathlib.Path(__file__).parent.resolve()
CONVERTED_FILES_DIR = os.path.join(BASE_DIR, 'tmp')
os.makedirs(CONVERTED_FILES_DIR, exist_ok=True)
