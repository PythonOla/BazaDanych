from json import load
from json import dumps #słownik -> string

#uwaga! Ola nie jest ściezką
BASE_PATH = 'ola :)'
class Output:
    def __init__(self, data_base_path = BASE_PATH):
        self.data_base_path = data_base_path
        with open(data_base_path, 'r+', encoding='utf-8') as file:
            self.data = load(file)
            self.file = file
