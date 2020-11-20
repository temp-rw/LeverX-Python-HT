import os
from json import loads


class IParser:
    def create_data_path(self, file_path: str, file_name: str) -> str:
        pass

    def extract_text(self, full_file_name: str) -> dict:
        pass


class JSONParser(IParser):
    def __init__(self):
        self._cur_dir = os.getcwd()
        self.file = None
        self.parsed_text = None

    def create_data_path(self, file_path: str, file_name: str) -> str:
        """
        loads path where the file placed, change current working directory
        :param file_path: absolute path to json file
        :param file_name: file name
        :return:
        """
        full_file_name = os.path.join(file_path, file_name)
        return full_file_name

    def extract_text(self, full_file_name: str) -> dict or list:
        """
        Extracting json file to python dict if single, else to list
        :param full_file_name: string that consists of absolute path and file name
        :return: dict or list of dicts
        """
        with open(full_file_name, encoding='utf-8') as file:
            data = file.read()
        data = loads(data)
        return data
