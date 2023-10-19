class BaseServiceException(Exception):
    message = None

    def __init__(self, message: str = ''):
        if message:
            self.message = message

    def __str__(self):
        return self.message


class NotValidRequestData(BaseServiceException):
    pass


class FileNotTransferred(NotValidRequestData):
    message = 'Переданный файл не найден!'


class NotValidConvertFileType(NotValidRequestData):
    message = 'Невалдный тип конвертированного файла!'


class NotValidFileType(NotValidRequestData):
    message = 'Невалдный тип файла!'


class ConversionError(BaseServiceException):
    pass
