from typing import Union
import os
from json import loads


class IParser:
    def create_data_path(self, file_path: str, file_name: str) -> str:
        raise NotImplementedError

    def extract_text(self, full_file_name: str) -> dict:
        raise NotImplementedError


class JSONParser(IParser):
    def __init__(self):
        self._cur_dir = os.getcwd()
        self.file = None
        self.parsed_text = None

    def create_data_path(self, file_path: str, file_name: str) -> str:
        """
        Creates data path string
        :param file_path: absolute path to json file
        :param file_name: file name
        :return: file name with path
        """
        full_file_name = os.path.join(file_path, file_name)
        return full_file_name

    def extract_text(self, full_file_name: str) -> Union[dict, list]:
        """
        Extracting json file to python dict if single, else to list
        :param full_file_name: string that consists of absolute path and file name
        :return: dict or list of dicts
        """
        with open(full_file_name, encoding="utf-8") as file:
            data = file.read()
        data = loads(data)
        return data
