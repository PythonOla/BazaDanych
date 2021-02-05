from json import load
from ..Users import User_list
from ..likes import Like_list
from ..posts import Posts_list
from ..comments import Comments_list

#to do
#uwaga! Ola nie jest ściezką
BASE_PATH = 'ola :)'
class Input:
    def __init__(self, data_base_path = BASE_PATH):
        self.data_base_path = data_base_path
        with open(data_base_path, 'r', encoding='utf-8') as file:
            data = load(file)
            self.user_list = User_list(data["users"])
            self.likes_list = Like_list(data["likes"])
            self.posts_list = Posts_list(data["posts"])
            self.comments_list = Comments_list(data["comments"])
