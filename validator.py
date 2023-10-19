from exceptions import (
    FileNotTransferred,
    NotValidConvertFileType,
    NotValidFileType,
)
from settings import AVAILABLE_FORMATS


class Validator:
    def __init__(
            self,
            data: dict
    ):
        self.data = data

    def validate_data(self):
        self._validate_file()
        self._validate_file_type()
        self._validate_convert_file_type()

    def _validate_file(self):
        file = self.data.get('file')
        if file is None:
            raise FileNotTransferred

    def _validate_file_type(self):
        _, file_type = self.data.get('file').filename.split('.')
        if file_type.upper() not in AVAILABLE_FORMATS:
            raise NotValidFileType

    def _validate_convert_file_type(self):
        convert_type = self.data.get('to_type', 'pdf')
        if convert_type.upper() not in AVAILABLE_FORMATS:
            raise NotValidConvertFileType
