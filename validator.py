from exceptions import (
    FileNotTransferred,
    NotValidConvertFileType,
    NotValidFileType,
)
from settings import CONVERT_FILE_TYPES


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
        if file_type not in CONVERT_FILE_TYPES:
            raise NotValidFileType

    def _validate_convert_file_type(self):
        convert_type = self.data.get('type', 'pdf')
        if convert_type not in CONVERT_FILE_TYPES:
            raise NotValidConvertFileType
