from json import load
from user_list import User_list
from likes_list import Likes_list
from posts_list import Posts_list
from comments_list import Comments_list


class Input:
    def __init__(self, data_base_path):
        self.data_base_path = data_base_path
        with open(data_base_path, 'r', encoding='utf-8') as file:
            data = load(file)
            self.user_list = User_list(data["users"])
            self.likes_list = Likes_list(data["likes"])
            self.posts_list = Posts_list(data["posts"])
            self.comments_list = Comments_list(data["comments"])
