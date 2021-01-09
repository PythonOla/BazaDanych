from json import load
from user_list import User_list


class Input:
    def __init__(self, data_base_path):
        self.data_base_path = data_base_path
        with open(data_base_path, 'r', encoding='utf-8') as file:
            data = load(file)
            self.user_list = User_list(data["users"])
