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

    def _update_data_section(self, new_data, section_name):
        self.data[section_name] = new_data
        json_string = dumps(self.data)
        self.file.write(json_string)

    def update_users(self, data):
        self._update_data_section(data, 'users')

    def update_likes(self, data):
        self._update_data_section(data, 'likes')

    def update_posts(self, data):
        self._update_data_section(data, 'posts')

    def update_comments(self, data):
        self._update_data_section(data, 'comments')


    
