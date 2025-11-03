import json
from .constants import ROOT_FILE_PATH


class AppConfig:
    def __init__(self, file_path = ROOT_FILE_PATH):
        self.file_path = file_path

    def load_config(self):
        with open(self.file_path, 'r') as file_reader:
            data = json.load(file_reader)
            return data
