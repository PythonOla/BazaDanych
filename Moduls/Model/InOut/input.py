from json import load
from os import path
from sys import argv
from ..Users import User_list
from ..likes.likes_list import Like_list
from ..posts import Posts_list
from ..comments import Comments_list


BASE_PATH = path.join(path.dirname(argv[0]), 'baza.json')
class Input:
    def __init__(self, data_base_path = BASE_PATH):
        self.data_base_path = data_base_path
        with open(data_base_path, 'r', encoding='utf-8') as file:
            data = load(file)
            self.user_list = User_list(data["users"])
            self.likes_list = Like_list(data["likes"])
            self.posts_list = Posts_list(data["posts"])
            self.comments_list = Comments_list(data["comments"])
