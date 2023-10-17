class BaseServiceException(Exception):
    message = None

    def __init__(self, message: str = ''):
        if message:
            self.message = message

    def __str__(self):
        return self.message


class FileNotTransferred(BaseServiceException):
    message = 'Переданный файл не найден!.'


class NotValidConvertFileType(BaseServiceException):
    message = 'Невалдный тип конвертированного файла!'


class NotValidFileType(BaseServiceException):
    message = 'Невалдный тип файла!'


class ConversionError(BaseServiceException):
    pass
