import os


class ISaver:
    def save(self, data: str):
        raise NotImplementedError


class FileSaver(ISaver):
    def __init__(self, file_path: str, file_name: str, file_format: str, mode: str):
        self.file_path = file_path
        self.file_name = file_name
        self.file_format = file_format
        self.mode = mode
        self.file = None

    def save(self, data: str or bytes):
        with open(os.path.join(self.file_path, self.file_name + "." + self.file_format), self.mode) as self.file:
            self.file.write(data)
