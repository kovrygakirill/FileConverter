# About
```
FILE CONVERTER - SUPPORT FILE TYPES:

TEXT_DOCUMENTS = ['ODT', 'DOC', 'DOCX', 'RTF', 'TXT', 'HTML']
SPREADSHEETS = ['ODS', 'XLS', 'XLSX', 'CSV']
PRESENTATIONS = ['ODP', 'PPT', 'PPTX']
IMAGES = ['BMP', 'GIF', 'JPG', 'PNG', 'SVG']
OTHER_FORMATS = ['PDF', 'EPUB', 'SWF', 'XHTML']
```

# Requirements

python 3.10.6

# How to start?

1. Activate virtual environment
2. Add environment variables to environment or create `.env` file

```
SERVICE_PORT=="open port"
```

If you want start local server on Linux:

3. `pip install pipenv`
4. `pipenv install --dev`
5. `sudo apt-get update && sudo apt-get install -y libreoffice`
6. `python app.py`

If you want start docker image, run:
`sudo docker-compose up -d --build`

# Instructions for use

```
POST /convert

Headers:
- Content-Type: multipart/form-data

Body:
- file(required) - Example: hello.rtf
- to_type - Example: doc(default - pdf)
```
